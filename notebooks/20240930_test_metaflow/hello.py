from dotenv import load_dotenv
load_dotenv() 

from metaflow import FlowSpec, Parameter, step, batch

class ParameterFlow(FlowSpec):
    alpha = Parameter('alpha',
                      help='Learning rate',
                      default=0.01,
                      type=float)

    @step
    def start(self):
        print('alpha is %f' % self.alpha)
        self.next(self.end)

    @step
    def end(self):
        print('alpha is still %f' % self.alpha)

if __name__ == '__main__':
    ParameterFlow()