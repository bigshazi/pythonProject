import pytest


class TestDemo:
    def test_01(self):
        assert 1  # 断言成功

    def test_02(self):
        assert 0  # 断言失败

if __name__ == '__main__':
        pytest.main(['-s', '-vv', 'class0713.py','--alluredir', './report/xml'])