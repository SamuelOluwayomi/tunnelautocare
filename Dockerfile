# 1. Use official Python 3.12 image
FROM python:3.12-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the Django project files
COPY . .

# 5. Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8080

# 6. Collect static files
RUN python manage.py collectstatic --noinput

# 7. Expose the port Railway uses
EXPOSE 8080

# 8. Start the Gunicorn server
CMD ["gunicorn", "tunnelautocare.wsgi:application", "--bind", "0.0.0.0:8080"]
