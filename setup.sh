mkdir -p ~/.streamlit
echo "
[global]

# By default, Streamlit checks if the Python watchdog module is available and, if not, prints a warning asking for you to install it. The watchdog module is not required, but highly recommended. It improves Streamlit's ability to detect changes to files in your filesystem.
# If you'd like to turn off this warning, set this to True.
# Default: false
disableWatchdogWarning = false

# If True, will show a warning when you run a Streamlit-enabled script via 'python my_script.py'.
# Default: true
showWarningOnDirectExecution = true

# DataFrame serialization.
# Acceptable values: - 'legacy': Serialize DataFrames using Streamlit's custom format. Slow but battle-tested. - 'arrow': Serialize DataFrames using Apache Arrow. Much faster and versatile.
# Default: 'arrow'
dataFrameSerialization = 'arrow'

[logger]

# Level of logging: 'error', 'warning', 'info', or 'debug'.
# Default: 'info'
level = 'info'

# String format for logging messages. If logger.datetimeFormat is set, logger messages will default to `%(asctime)s.%(msecs)03d %(message)s`. See [Python's documentation](https://docs.python.org/2.6/library/logging.html#formatter-objects) for available attributes.
# Default: None
messageFormat = '%(asctime)s %(message)s'

[client]

# Whether to enable st.cache.
# Default: true
caching = true

# If false, makes your Streamlit script not draw to a Streamlit app.
# Default: true
displayEnabled = true

# Controls whether uncaught app exceptions are displayed in the browser. By default, this is set to True and Streamlit displays app exceptions and associated tracebacks in the browser.
# If set to False, an exception will result in a generic message being shown in the browser, and exceptions and tracebacks will be printed to the console only.
# Default: true
showErrorDetails = false

[runner]

# Allows you to type a variable or string by itself in a single line of Python code to write it to the app.
# Default: true
magicEnabled = true

# Install a Python tracer to allow you to stop or pause your script at any point and introspect it. As a side-effect, this slows down your script's execution.
# Default: false
installTracer = false

# Sets the MPLBACKEND environment variable to Agg inside Streamlit to prevent Python crashing.
# Default: true
fixMatplotlib = true

# Run the Python Garbage Collector after each script execution. This can help avoid excess memory use in Streamlit apps, but could introduce delay in rerunning the app script for high-memory-use applications.
# Default: true
postScriptGC = false

[server]

# List of folders that should not be watched for changes. This impacts both "Run on Save" and @st.cache.
# Relative paths will be taken as relative to the current working directory.
# Example: ['/home/user1/env', 'relative/path/to/folder']
# Default: []
folderWatchBlacklist = []

# Change the type of file watcher used by Streamlit, or turn it off completely.
# Allowed values: * 'auto' : Streamlit will attempt to use the watchdog module, and falls back to polling if watchdog is not available. * 'watchdog' : Force Streamlit to use the watchdog module. * 'poll' : Force Streamlit to always use polling. * 'none' : Streamlit will not watch files.
# Default: 'auto'
fileWatcherType = 'none'

# Symmetric key used to produce signed cookies. If deploying on multiple replicas, this should be set to the same value across all replicas to ensure they all share the same secret.
# Default: randomly generated secret key.
cookieSecret = '8f977825ef28021786956c69468624eb33cf6c6784f07d5eda52d0605de1eb96'

# If false, will attempt to open a browser window on start.
# Default: false unless (1) we are on a Linux box where DISPLAY is unset, or (2) server.liveSave is set.
headless = true

# Automatically rerun script when the file is modified on disk.
# Default: false
runOnSave = false

# The address where the server will listen for client and browser connections. Use this if you want to bind the server to a specific address. If set, the server will only be accessible from this address, and not from any aliases (like localhost).
# Default: (unset)
#address =

# The port where the server will listen for browser connections.
# Default: 8501
port = $PORT

# The base path for the URL where Streamlit should be served from.
# Default: ""
baseUrlPath = ""

# Enables support for Cross-Origin Request Sharing (CORS) protection, for added security.
# Due to conflicts between CORS and XSRF, if `server.enableXsrfProtection` is on and `server.enableCORS` is off at the same time, we will prioritize `server.enableXsrfProtection`.
# Default: true
enableCORS = true

# Enables support for Cross-Site Request Forgery (XSRF) protection, for added security.
# Due to conflicts between CORS and XSRF, if `server.enableXsrfProtection` is on and `server.enableCORS` is off at the same time, we will prioritize `server.enableXsrfProtection`.
# Default: true
enableXsrfProtection = true

# Max size, in megabytes, for files uploaded with the file_uploader.
# Default: 200
maxUploadSize = 10

# Enables support for websocket compression.
# Default: true
enableWebsocketCompression = true

[browser]

# Internet address where users should point their browsers in order to connect to the app. Can be IP address or DNS name and path.
# This is used to: - Set the correct URL for CORS and XSRF protection purposes. - Show the URL on the terminal - Open the browser - Tell the browser where to connect to the server when in liveSave mode.
# Default: 'localhost'
serverAddress = 'localhost'

# Whether to send usage statistics to Streamlit.
# Default: true
gatherUsageStats = true

# Port where users should point their browsers in order to connect to the app.
# This is used to: - Set the correct URL for CORS and XSRF protection purposes. - Show the URL on the terminal - Open the browser - Tell the browser where to connect to the server when in liveSave mode.
# Default: whatever value is set in server.port.
serverPort = $PORT

[mapbox]

# Configure Streamlit to use a custom Mapbox token for elements like st.pydeck_chart and st.map. To get a token for yourself, create an account at https://mapbox.com. It's free (for moderate usage levels)!
# Default: ''
token = ''

[deprecation]

# Set to false to disable the deprecation warning for the file uploader encoding.
# Default: true
showfileUploaderEncoding = false

# Set to false to disable the deprecation warning for using the global pyplot instance.
# Default: true
showPyplotGlobalUse = false

[theme]

# The preset Streamlit theme that your custom theme inherits from. One of "light" or "dark".
base = 'light'

# Primary accent color for interactive elements.
primaryColor = '#f72585'

# Background color for the main content area.
backgroundColor = '#f8f8f8'

# Background color used for the sidebar and most interactive widgets.
backgroundColor = '#ffffff'

# Color used for almost all text.
textColor = '#3a0ca3'

# Font family for all text in the app, except code blocks. One of 'sans serif', 'serif', or 'monospace'.
font = 'sans serif'

" > ~/.streamlit/config.toml

mkdir -p ~/firebase
echo '
{
  "type": "service_account",
  "project_id": "jaka-id",
  "private_key_id": "3ffa94ea6f43c1be7b2aaf222c655c94b2ae89a9",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDODM01yaRGaojb\nAccFnbuCiHMndvLGSxYFcdl6hunDAx7jux/Rn93kmSEVIIcgK5eoDhyjxjcaRNWi\nSany72gYquRZ5SRf3o5jW8b6/TDvkT6SC/3nC274uTKPudcq1OF4KmoEs5c9wifV\n4OziXEJxITS5wk6/1mby/9amYkjBhc9ZIydt73PllHzywI9AoBbZLF7dvamlgiUJ\nAs5NK1cSOBnN8cJsPTpXJRAbKH67B9tDK6WuL3nuPR85TrmGeoO2LkRiJhUoLuxh\nnZWrNOetVeeGk9d4v0Oet6QGE2zMHZxtLaE451MjcKNxG9nvcC2gLHGxRdzQtlEZ\n7Raac9B/AgMBAAECggEACF6Qv0yPdaTCJlMuKFY91ZGBS+sS9Wb7YAE92jI8sIUh\n7hIdusAJnU1zAI6vrmjW4iagly5n8pM1MkBXvNxomAfo+pXKInLBydtie7NpF3II\n3pnKGGZofYXYPepIiR7Yga8HW2WIESQfxho6xP8GW94DbEAuPrCQwfIOX/fCCMo5\n3HVw4C7cA7PisleplA76L6gar4bcPK3N6nrE88fzD6Ib0J2EvOlPiN73eyL81YUO\n5k24yQQdO8G0OqSWPMPu7MM7gH3oLmIC7N8LdQwuApyeaRSK0DoB/wZOEfr8dwxC\nDbnx021b6F6d5f9m2W0BIqWGps3gZtGTqLZwwM0oAQKBgQD/aPVhzmdKcreIDADV\nUKUWs0aMF6prVuhc+Wyq30TuPtiuo2n1mcUHLxnyXVpYv0xQ5fGPfA7fba1t3oaR\nuVDPhqBvwAccnLXf1X4bYnFfOd9a+2wzYDvn+7TnKpVsN5FTbkwcjJLyw4qYR0q1\neLTz5cHYJNNveJuMqQHhtUsCfwKBgQDOhqczSotpopJ75lRo/ZU7ImhjD8ijtnVf\nZwiiIE06gz+LN3srBpaLzl3JfPFZSdTjejXAJoAruo6KRuSJYNxqEboK5hKYu7sW\nRYnO50i4dYSvADI60E7UIeyDg34m2hqzW/jVg9Mws4O73JCg03OfUMKQq1zE+5e9\nfTgAE1QyAQKBgQD5/DAYT953VrreFOmH4AwFoOjO26b4srJxtcuvnyInkimhHN7r\n/VqEQozB1K9GJ865a6a4SrN/6iiSXfgWj2xSArHrTudnENdOwvZQNVVD4DAGLAnm\nay2XTJzumZZwuh6qq00hsFFv/QYdL8ImxoNOKTZGqRytgT22OgFWeox1XwKBgDNX\nPhF+IpIsHAY5CBrhj0uYDiMyNUqdfSguUPMc3JYDMrTFIhVcGei/cIk6SjVMKWQz\naVFPQOWeBvlRDlcogSLNLVawQ0c8xBGRT+Tjkixo6ocmoVYFmtMZa9Z1xdKavbCA\n2KcbklC1D7aP6lRQvJmKVhPoxbMiaGJu0pESPQgBAoGAUTJ224idLgafg0kKuYff\nKxe7XISDRvR90Ab5TEn3E582Rl+u6Osx3W/PPV1FhmYt6srfOQhX2DpScFr/pPUP\nU8V4YWzBK+adbfHW0Mhv3vvO2NgcSbibwUE3e9saV73++rSPSXN4W4IhfFw/7555\nwl/DuLZv63Esa6gytDXgkh0=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-e83r3@jaka-id.iam.gserviceaccount.com",
  "client_id": "105991201552807563925",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-e83r3%40jaka-id.iam.gserviceaccount.com"
}
' > ~/firebase/serviceAccountKey.json
