from sklearn.ensemble import RandomForestClassifier

from explainerdashboard import ClassifierExplainer, ExplainerDashboard
from explainerdashboard.datasets import titanic_survive, feature_descriptions

X_train, y_train, X_test, y_test = titanic_survive()
model = RandomForestClassifier(n_estimators=50, max_depth=10).fit(X_train, y_train)

explainer = ClassifierExplainer(
    model, X_test, y_test,
    # optional:
    cats=['Sex', 'Deck', 'Embarked'],
    labels=['Not survived', 'Survived'])
# calculate properties needed for this dashboard:
db = ExplainerDashboard(explainer)
# alternatively:
# explainer.calculate_properties()
explainer.dump("explainer.joblib")

#%%
