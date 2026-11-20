import time
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Callable
from functools import wraps
from sklearn.base import BaseEstimator
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score

# ==========================================
# 1. FACTORY PATTERN
# ==========================================
class ModelFactory:
    """Factory klasa za kreiranje ML modela."""
    
    _models = {
        "linear": LogisticRegression,
        "tree": DecisionTreeClassifier,
        "knn": KNeighborsClassifier
    }

    @classmethod
    def create_model(cls, model_type: str, **kwargs) -> BaseEstimator:
        if model_type not in cls._models:
            raise ValueError(f"Nepoznat tip modela: {model_type}. Dostupno: {list(cls._models.keys())}")
        return cls._models[model_type](**kwargs)

# ==========================================
# 2. STRATEGY PATTERN (Metrike)
# ==========================================
class MetricStrategy(ABC):
    @abstractmethod
    def calculate(self, y_true: List[int], y_pred: List[int]) -> float:
        pass

class AccuracyStrategy(MetricStrategy):
    def calculate(self, y_true: List[int], y_pred: List[int]) -> float:
        return accuracy_score(y_true, y_pred)

class F1Strategy(MetricStrategy):
    def calculate(self, y_true: List[int], y_pred: List[int]) -> float:
        return f1_score(y_true, y_pred, average='weighted')

# ==========================================
# 3. OBSERVER PATTERN (Praćenje treninga)
# ==========================================
class Observer(ABC):
    @abstractmethod
    def update(self, event: str, data: Dict[str, Any]) -> None:
        pass

class ConsoleLogger(Observer):
    def update(self, event: str, data: Dict[str, Any]) -> None:
        if event == "start":
            print(f"[LOG] Započinjem eksperiment sa modelom: {data.get('model')}")
        elif event == "end":
            print(f"[LOG] Završen eksperiment. Rezultati: {data.get('metrics')}")

# ==========================================
# 4. DECORATOR PATTERN (Merenje vremena)
# ==========================================
def measure_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        if isinstance(result, dict):
            result["vreme_izvrsavanja_sek"] = round(end_time - start_time, 4)
        return result
    return wrapper

# ==========================================
# 5. TEMPLATE METHOD PATTERN (Tok eksperimenta)
# ==========================================
class ExperimentTemplate(ABC):
    def __init__(self, metric_strategy: MetricStrategy):
        self.metric_strategy = metric_strategy
        self.observers: List[Observer] = []

    def attach_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def _notify(self, event: str, data: Dict[str, Any]) -> None:
        for obs in self.observers:
            obs.update(event, data)

    @measure_time
    def run(self, X_train, y_train, X_test, y_test, model_type: str, **model_kwargs) -> Dict[str, Any]:
        self._notify("start", {"model": model_type})
        
        # 1. Kreiraj model (Factory)
        model = ModelFactory.create_model(model_type, **model_kwargs)
        
        # 2. Treniraj
        model.fit(X_train, y_train)
        
        # 3. Predvidi
        predictions = model.predict(X_test)
        
        # 4. Izračunaj metrike (Strategy)
        score = self.metric_strategy.calculate(y_test, predictions)
        
        results = {
            "model": model_type,
            "metrika": score,
            "metric_type": self.metric_strategy.__class__.__name__
        }
        
        self._notify("end", {"metrics": results})
        return results
