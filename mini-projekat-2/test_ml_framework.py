import pytest
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from ml_framework import ModelFactory, AccuracyStrategy, F1Strategy, ConsoleLogger, ExperimentTemplate

@pytest.fixture
def iris_data():
    data = load_iris()
    return train_test_split(data.data, data.target, test_size=0.3, random_state=42)

def test_factory():
    assert ModelFactory.create_model("linear").__class__.__name__ == "LogisticRegression"
    with pytest.raises(ValueError): ModelFactory.create_model("nepostojeci")

def test_strategy(iris_data):
    X_train, X_test, y_train, y_test = iris_data
    model = ModelFactory.create_model("knn", n_neighbors=3)
    model.fit(X_train, y_train)
    assert 0.0 <= AccuracyStrategy().calculate(y_test, model.predict(X_test)) <= 1.0

def test_observer(iris_data, capsys):
    X_train, X_test, y_train, y_test = iris_data
    exp = ExperimentTemplate(AccuracyStrategy())
    exp.attach_observer(ConsoleLogger())
    exp.run(X_train, y_train, X_test, y_test, "linear")
    assert "[LOG] Započinjem" in capsys.readouterr().out

def test_full_pipeline(iris_data):
    X_train, X_test, y_train, y_test = iris_data
    results = ExperimentTemplate(AccuracyStrategy()).run(X_train, y_train, X_test, y_test, "tree", max_depth=3)
    assert "vreme_izvrsavanja_sek" in results and results["metrika"] > 0.8

def test_f1(iris_data):
    X_train, X_test, y_train, y_test = iris_data
    model = ModelFactory.create_model("tree", max_depth=3)
    model.fit(X_train, y_train)
    assert 0.0 <= F1Strategy().calculate(y_test, model.predict(X_test)) <= 1.0
