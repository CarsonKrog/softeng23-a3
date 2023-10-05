import pytest

from pmgr.project import Project, TaskException

@pytest.fixture(scope="function")
def testproj():
    tproj = Project('mytestproj')
    yield tproj
    tproj.delete()

def test_add(testproj):
    testproj.add_task('dosomething')
    assert 'dosomething' in testproj.get_tasks()

def test_fail_add(testproj):
    testproj.add_task('dosomething')
    with pytest.raises(TaskException):
        testproj.add_task('dosomething')

def test_remove(testproj):
    testproj.add_task('dosomething')
    testproj.remove_task('dosomething')
    assert 'dosomething' not in testproj.get_tasks()

def test_fail_remove(testproj):
    with pytest.raises(TaskException):
        testproj.remove_task('dosomething')

