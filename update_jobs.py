import requests

API_KEY = "WcKXyCAzzvDQV3Z4yKMnZex5CwPeQJbCrhL0PmKacgjE8FRELDpW"
response = requests.get(f"https://oapi.saramin.co.kr/job-search?access-key={API_KEY}&keywords=개발자&count=10")
data = response.json()
jobs = data.get("jobs", {}).get("job", [])

html_content = """
<!DOCTYPE html>
<html>
<head>
  <title>개발자 취업 달력</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f4f4f9; padding: 20px; }
    h1 { text-align: center; color: #333; }
    .job-list { max-width: 600px; margin: 0 auto; }
    .job-card { background: #fff; padding: 15px; margin: 10px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); }
  </style>
</head>
<body>
  <h1>개발자 취업 달력</h1>
  <div class="job-list">
"""

for job in jobs:
    title = job.get("position", {}).get("title", "제목 없음")
    company = job.get("company", {}).get("detail", {}).get("name", "기업명 없음")
    location = job.get("position", {}).get("location", {}).get("name", "지역 없음")
    url = f"https://www.saramin.co.kr/zf_user/jobs/relay/view?rec_idx={job.get('id', '')}"
    html_content += f"""
      <div class="job-card">
        <h2>{title}</h2>
        <p>기업명: {company}</p>
        <p>근무지역: {location}</p>
        <a href="{url}" target="_blank">공고 링크</a>
      </div>
    """

html_content += "</div></body></html>"

# HTML 파일 생성
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)
