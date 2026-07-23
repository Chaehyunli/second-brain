from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import enrich_tistory_blog_bodies as enrich


class TistoryBodyEnrichmentTests(unittest.TestCase):
    def test_classifies_course_post_as_tutorial(self):
        self.assertEqual(
            enrich.classify_post("[스프링 DB] JdbcTemplate 소개", "INFLEARN", []),
            "tutorial",
        )

    def test_course_category_wins_over_generic_problem_word_in_body(self):
        self.assertEqual(
            enrich.classify_post("스프링 JdbcTemplate", "INFLEARN", [("text", "문제 상황과 해결 방법을 학습한다.")]),
            "tutorial",
        )

    def test_classifies_error_post_as_troubleshooting(self):
        self.assertEqual(
            enrich.classify_post("Spring Boot CORS 중복 응답 문제 해결", "SPRING BOOT", []),
            "troubleshooting",
        )

    def test_render_keeps_full_frontmatter_and_related_links(self):
        frontmatter = "---\ntitle: \"테스트\"\nsource_url: https://ch010104.tistory.com/1\n---\n\n"
        old_body = "# 테스트\n\n## 관련 글\n\n- [[blog/SPRING BOOT/index|SPRING BOOT]]\n"
        blocks = [
            ("heading", "문제 상황"),
            ("text", "JdbcTemplate을 적용하면 JDBC 자원 관리의 반복 코드를 줄일 수 있습니다."),
            ("heading", "구현 코드"),
            ("code", "JdbcTemplate template = new JdbcTemplate(dataSource);"),
        ]
        result = enrich.render_note(frontmatter, old_body, "테스트", "tutorial", blocks)
        self.assertTrue(result.startswith(frontmatter))
        self.assertIn("## 원문\n\nhttps://ch010104.tistory.com/1", result)
        self.assertIn("## 학습 목표 및 맥락", result)
        self.assertIn("## 원문 기반 학습 정리", result)
        self.assertIn("```java", result)
        self.assertIn("[[blog/SPRING BOOT/index|SPRING BOOT]]", result)

    def test_render_troubleshooting_uses_incident_template(self):
        result = enrich.render_note(
            "---\ntitle: \"오류\"\n---\n\n", "# 오류\n", "오류", "troubleshooting",
            [("heading", "증상"), ("text", "CORS 헤더가 중복되어 브라우저 요청이 실패합니다.")],
        )
        self.assertIn("## 문제·재현 맥락", result)
        self.assertIn("## 원인·해결 근거", result)

    def test_literalizes_array_style_wikilinks_in_prose(self):
        result = enrich.render_note(
            "---\ntitle: \"배열\"\n---\n\n", "# 배열\n", "배열", "concept",
            [("text", "NumPy 결과는 [[100, 200]]처럼 표시될 수 있습니다.")],
        )
        self.assertIn(r"\[\[100, 200\]\]", result)
        self.assertNotIn("\nNumPy 결과는 [[100, 200]]", result)
    def test_literalizes_html_tags_in_prose(self):
        result = enrich.render_source_structure([
            ("text", "여러 요소(<h2>, <p> 등)를 하나의 <div>로 묶습니다."),
        ])
        self.assertIn("`<h2>`", result)
        self.assertIn("`<p>`", result)
        self.assertIn("`<div>`", result)
        self.assertNotIn("여러 요소(<h2>", result)
    def test_literalizes_html_tags_only_outside_fenced_code(self):
        source = "### HTML Div - <div>\n\n여러 요소(<h2>, <p>)를 묶습니다.\n\n```html\n<div><h2>Example</h2></div>\n```\n"
        result = enrich.literalize_html_tags_in_markdown(source)
        self.assertIn("### HTML Div - `<div>`", result)
        self.assertIn("요소(`<h2>`, `<p>`)", result)
        self.assertIn("```html\n<div><h2>Example</h2></div>\n```", result)


if __name__ == "__main__":
    unittest.main()
