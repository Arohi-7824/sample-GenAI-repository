"""
Data model for the Flask AI project.
"""

from datetime import datetime

class DataModel:
    """Data model class for representing data in the Flask AI project."""
    def __init__(self):
        self.data_store={}

    def get_timestamp(self):
        return datetime.utcnow().isoformat()
    
    def process_text(self, text,options=None):
        if options is None:
            options = {}
        result=text

        if options.get('uppercase',default=False):
            result=result.upper()

        if options.get('lowercase',default=False):
            result=result.lower()

        if options.get('reverse',default=False):
            result=result[::-1]

        if options.get('remove_spaces',default=False):
            result=result.replace(" ", "")

        return result
    
    def calculate(self,operation,numbers):
        if not numbers:
            raise ValueError("Numbers list cannot be empty.")
        
        if operation == 'add':
            return sum(numbers)
        
        elif operation == 'multiply':
            result=1
            for num in numbers:
                result *= num
            return result
        
        elif operation == 'average':
            return sum(numbers)/len(numbers)
        
        elif operation == 'max':
            return max(numbers)
        
        elif operation == 'min':
            return min(numbers)
        
        else:
            raise ValueError(f"Unsupported operation: {operation}") 
        

        def store_data(self,key,value):
            self.data_store[key]={
                'value':value,
                'timestamp':self.get_timestamp()      
            }

        def get_data(self,key):
            return self.data_store.get(key,None)