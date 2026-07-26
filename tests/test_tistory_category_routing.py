from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from rebuild_tistory_blog import category_of


class TistoryCategoryRoutingTests(unittest.TestCase):
    def test_studying_title_routes_when_tistory_category_metadata_is_missing(self):
        self.assertEqual(category_of("<html></html>", "[STUDYING] 8. HTML, CSS, JavaScript_Day2"), "STUDYING")

    def test_inflearn_course_title_routes_when_tistory_category_metadata_is_missing(self):
        self.assertEqual(
            category_of("<html></html>", "[스프링 DB 2편 - 데이터 접근 활용 기술] 7. 데이터 접근 기술 - Querydsl"),
            "INFLEARN",
        )

    def test_tistory_entry_category_label_has_priority_over_service_section(self):
        source = '''
        window.T.entryInfo = {"entryId":316,"categoryId":1321517,"categoryLabel":"INFLEARN"};
        <meta property="article:section" content="IT 인터넷">
        '''
        self.assertEqual(category_of(source, "[아무 제목]"), "INFLEARN")


if __name__ == "__main__":
    unittest.main()
