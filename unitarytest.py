import unittest
import time
import sys

class CustomTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.global_start_time = None

    def startTest(self, test):
        self.start_time = time.time()
        super().startTest(test)
        
        if self.global_start_time is None:
            module_name = test.__class__.__module__
            self.global_start_time = self.start_time
            self.module_name = test.__class__.__module__
            self.class_name  = test.__class__.__name__

            msg = f"""##########################################
### Started Test on  {self.module_name}.{self.class_name} ###
##########################################\n""" 
            sys.stdout.write(msg)

    def addSuccess(self, test):
        super().addSuccess(test)
        self.show_result(test, "OK")

    def addError(self, test, err):
        super().addError(test, err)
        self.show_result(test, "Echec")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.show_result(test, "Echec")

    def show_result(self, test, result):
        elapsed_time = time.time() - self.start_time
        method_name = test._testMethodName
        formatted_method_name = f"{self.module_name}.{self.class_name}.{method_name:<20}"
        sys.stdout.write(f"\nTesting: {formatted_method_name}: run in {elapsed_time:.5f}s; {result}")
        sys.stdout.flush()
        sys.stdout.flush()

def run(iterable):
    for i,obj in enumerate(iterable):
        if i > 0:
            sys.stdout.write("\n")

        suite = unittest.TestLoader().loadTestsFromTestCase(obj)

        # Utiliser buffer=True et failfast=True
        runner = unittest.TextTestRunner(resultclass=CustomTestResult, stream=sys.stdout, verbosity=1)
    
        # Exécuter les tests
        result = runner.run(suite)
