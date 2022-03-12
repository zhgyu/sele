import unittest
loader = unittest.TestLoader().discover('test',pattern='test*.py')
runner = unittest.TextTestRunner()
runner.run(loader)