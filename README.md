# JAKA
JAKA is a short term of "Jadwal Aman Kuliah Aman" which is a web scheduling application for students of Universitas Indonesia planning their next term schedule.

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/chalimmm/jaka jaka

# Go into the repository
$ cd jaka

# Create Virtual Environment
$ python -m venv jaka

# Activate Virtual Environment
$ ./jaka/Scripts/activate

# Install dependencies
$ pip install -r requirements.txt

# Run the app
$ streamlit run index.py
```

> **Note**
> If there is error on protobuf version, please downgrade using
```bash
$ pip install 'protobuf<=3.20.1' --force-reinstall
```

## Credits

This software uses the following open source packages:

- [Streamlit](https://docs.streamlit.io/)
- [Selenium](https://www.selenium.dev/)

---
