import unittest
from unittest.mock import Mock, patch

import handler


class TwitterBackendTest(unittest.TestCase):
    def test_format_twitter_status_removes_markdown_markers(self):
        self.assertEqual(
            handler.format_twitter_status("*BTC* `_breakout_`"), "BTC breakout"
        )

    def test_xquik_requires_key_and_account(self):
        for api_key, account in (("", "account"), ("key", "")):
            with self.subTest(api_key=api_key, account=account):
                with patch.object(
                    handler.config, "xquik_api_key", api_key
                ), patch.object(handler.config, "xquik_account", account):
                    with self.assertRaisesRegex(
                        ValueError, "XQUIK_API_KEY and XQUIK_ACCOUNT are required"
                    ):
                        handler.send_xquik_alert("alert")

    def test_xquik_posts_clean_text_with_idempotency_key(self):
        response = Mock()
        response.json.return_value = {"status": "success"}
        request_id = Mock(hex="0123456789abcdef")

        with patch.object(handler.config, "xquik_api_key", "test-key"), patch.object(
            handler.config, "xquik_account", "connected-account"
        ), patch.object(handler.config, "xquik_timeout", 12), patch.object(
            handler.config, "xquik_api_url", "https://xquik.test/tweets"
        ), patch.object(
            handler, "uuid4", return_value=request_id
        ), patch.object(
            handler.requests, "post", return_value=response
        ) as post:
            result = handler.send_xquik_alert("*BTC* `_breakout_`")

        post.assert_called_once_with(
            "https://xquik.test/tweets",
            headers={
                "x-api-key": "test-key",
                "Idempotency-Key": "tradingview-0123456789abcdef",
            },
            json={"account": "connected-account", "text": "BTC breakout"},
            timeout=12,
        )
        response.raise_for_status.assert_called_once_with()
        self.assertEqual(result, {"status": "success"})

    def test_tweepy_preserves_credentials_and_text_cleanup(self):
        with patch.object(handler.config, "tw_ckey", "consumer-key"), patch.object(
            handler.config, "tw_csecret", "consumer-secret"
        ), patch.object(handler.config, "tw_atoken", "access-token"), patch.object(
            handler.config, "tw_asecret", "access-secret"
        ), patch.object(
            handler.tweepy, "OAuthHandler"
        ) as oauth_handler, patch.object(
            handler.tweepy, "API"
        ) as api:
            api.return_value.update_status.return_value = "posted"
            result = handler.send_tweepy_alert("*BTC* `_breakout_`")

        oauth_handler.assert_called_once_with("consumer-key", "consumer-secret")
        oauth_handler.return_value.set_access_token.assert_called_once_with(
            "access-token", "access-secret"
        )
        api.assert_called_once_with(oauth_handler.return_value)
        api.return_value.update_status.assert_called_once_with(status="BTC breakout")
        self.assertEqual(result, "posted")

    def test_backend_router_preserves_tweepy_default(self):
        with patch.object(handler.config, "twitter_backend", "tweepy"), patch.object(
            handler, "send_tweepy_alert", return_value="posted"
        ) as send_tweepy:
            self.assertEqual(handler.send_twitter_alert("alert"), "posted")
        send_tweepy.assert_called_once_with("alert")

        with patch.object(handler.config, "twitter_backend", "xquik"), patch.object(
            handler, "send_xquik_alert", return_value="posted"
        ) as send_xquik:
            self.assertEqual(handler.send_twitter_alert("alert"), "posted")
        send_xquik.assert_called_once_with("alert")

        with patch.object(handler.config, "twitter_backend", "unsupported"):
            with self.assertRaisesRegex(ValueError, "TWITTER_BACKEND"):
                handler.send_twitter_alert("alert")


if __name__ == "__main__":
    unittest.main()
