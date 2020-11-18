# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : vsnz                    #
# File Name             : config.py               #
# ----------------------------------------------- #

# Alert message in TradingView (ex. https://i.imgur.com/RFkuf1d.png)
# !! Case insensitive !!
whitelisted = [
    'buy alert', 'sell alert'
    ]

sec_code = ''

# Telegram Settings
send_telegram_alerts = False
tg_token   = ''  # Bot token. Get it from @Botfather
channel    = 0   # Channel ID (ex. -1001487568087)

# Discord Settings
send_discord_alerts = False
discord_webhook     = ''    # Discord Webhook URL (https://support.discordapp.com/hc/de/articles/228383668-Webhooks-verwenden)

#Twitter Settings
send_twitter_alerts = False
tw_ckey    = ''
tw_csecret = ''
tw_atoken  = ''
tw_asecret = ''

# Email Settings
send_email_alerts = False
email_sender      = ''        # Your email address
email_receivers   = ['', '']  # Receivers, can be multiple
email_subject     = 'Trade Alert!'

email_port        = 465       # SMTP SSL Port (ex. 465)
email_host        = ''        # SMTP host (ex. smtp.gmail.com)
email_user        = ''        # SMTP Login credentials
email_password    = ''        # SMTP Login credentials