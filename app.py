from flask import Flask, render_template, request
import json
from time import time

app = Flask(__name__)

class FibonacciCalculator:
    def __init__(self):
        self.cache = {0: {'value': 0, 'source': 'base case'}, 
                      1: {'value': 1, 'source': 'base case'}}
        self.calculation_log = []
    
    def fibonacci(self, n):
        if n in self.cache:
            self.calculation_log.append({
                'n': n,
                'value': self.cache[n]['value'],
                'source': 'cached',
                'time': time()
            })
            return self.cache[n]['value']
        
        # Calcula recursivamente
        value = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        
        # Armazena no cache
        self.cache[n] = {
            'value': value,
            'source': 'new calculation'
        }
        
        self.calculation_log.append({
            'n': n,
            'value': value,
            'source': 'new calculation',
            'time': time()
        })
        
        return value
    
    def get_sequence(self, n):
        self.calculation_log = []  # Mantém o cache, mas reseta o log
        
        if n < 0:
            return []
        
        # Garante que todos os valores até n sejam calculados
        self.fibonacci(n)
        
        # Gera a sequência completa
        sequence = []
        for i in range(n + 1):
            sequence.append({
                'n': i,
                'value': self.cache[i]['value'],
                'source': self.cache[i]['source']
            })
        
        return sequence

calculator = FibonacciCalculator()

@app.route('/', methods=['GET', 'POST'])
def index():
    sequence = []
    calculation_log = []
    n = 0
    
    if request.method == 'POST':
        n = int(request.form['number'])
        sequence = calculator.get_sequence(n)
        calculation_log = calculator.calculation_log
    
    return render_template('index.html', 
                           sequence=sequence,
                           calculation_log=calculation_log,
                           n=n)

if __name__ == '__main__':
    app.run(debug=True)
