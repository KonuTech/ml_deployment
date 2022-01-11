FROM python:3.9

RUN pip install explainerdashboard

COPY generate_dashboard.py ./
COPY run_dashboard.py ./

RUN python generate_dashboard.py

EXPOSE 8050
CMD ["python", "./run_dashboard.py"]