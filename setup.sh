mkdir -p ~/.streamlit
echo "[server]
headless = true
port = $PORT
enableCORS = false

[theme]
base = 'light'
primaryColor = '#f72585'
backgroundColor = '#f8f8f8'
textColor = '#3a0ca3'
font = 'sans serif'
" > ~/.streamlit/config.toml
