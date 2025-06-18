FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install pip dependencies separately to leverage cache
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all app code AFTER installing requirements
COPY . .

# Set PYTHONPATH
ENV PYTHONPATH=/app
ENV STREAMLIT_WATCH_DIRECTORIES=false

# Pre-build assets to avoid doing it at runtime
RUN python data/sample_reports/make_sample_report.py && \
    python src/build_kb.py

# Expose Streamlit port
EXPOSE 8501

# Default command
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
