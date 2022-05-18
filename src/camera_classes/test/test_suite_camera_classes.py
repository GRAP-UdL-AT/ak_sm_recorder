"""
Project:
Author:
Date:
Description:
...

Use:
"""

import unittest
from test_job_thread_azure import TestJobThreadAzure
from test_job_thread_3D_azure import TestJobThread3DAzure

def camera_management_suite():
    """
        Gather all the tests for Azure camera
    """
    test_suite = unittest.TestSuite()
    #test_suite.addTest(unittest.makeSuite(TestDatasetConfig))
    test_suite.addTest(unittest.makeSuite(TestJobThreadAzure))
    test_suite.addTest(unittest.makeSuite(TestJobThread3DAzure))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(camera_management_suite())