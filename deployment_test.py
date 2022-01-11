from explainerdashboard import ClassifierExplainer, ExplainerDashboard

#load the saved model
explainer = ClassifierExplainer.from_file("explainer.joblib")
db = ExplainerDashboard(explainer, title="Cool Title").run(use_waitress=True)
# need to define app so that gunicorn can find the flask server
app = db.flask_server()