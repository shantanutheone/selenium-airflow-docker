FROM python:3.9-slim

# Install necessary packages
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    apt-transport-https \
    unzip \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome browser
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Download and install ChromeDriver
RUN wget -q -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/linux64/chromedriver-linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Install Selenium and other Python dependencies
RUN pip install selenium

RUN pip install flask

# Set up display environment variables
ENV DISPLAY=:99

# Run a script that keeps the container alive
COPY keep_alive.sh /usr/local/bin/keep_alive.sh
RUN chmod +x /usr/local/bin/keep_alive.sh

CMD ["bash", "/usr/local/bin/keep_alive.sh"]
