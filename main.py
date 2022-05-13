import sys
sys.path.append("..")

from IOET.parser import Parser
from IOET.processor import Processor


parser = Parser('input.txt')
data = parser.get_data()

processor = Processor()
result = processor.process_data(data)

print(result)