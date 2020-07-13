import os
import unittest
import HtmlTestRunner
# from Src.TestClasses import LoginTestCase, MLoginTestCase1
import Src.TestClasses as testClass

class Main(unittest.TestCase):

    login_test = unittest.TestLoader().loadTestsFromTestCase(testClass.LoginTestCase)
    # login_test1 = unittest.TestLoader().loadTestsFromTestCase(MLoginTestCase1)

    test_suite = unittest.TestSuite([login_test])
    # test_suite = unittest.TestSuite([login_test, login_test1])

    basePath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # print(os.path.join(basePath, "Reports\\"))
    runner = HtmlTestRunner.HTMLTestRunner(output=os.path.join(basePath, "Reports\\"), report_title='Test Report Title', descriptions=True, template=os.path.join(basePath, "SampleTemplet\\testSample.html"))
    # outfile = open('C:\\Users\\buchusac\\PycharmProjects\\TestProjPageFactory\\Reports\\TestReport.html', 'w')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report Title', description='Test Description')

    runner.run(test_suite)

    # unittest.skipUnless()

if __name__ == '__main__':
    Main()
