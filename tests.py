import pytest

@pytest.mark.parametrize("expected_min, expected_max", [(12, 20)])
def test_course_duration_min_max(expected_min, expected_max):
    durations = [14, 20, 12, 20]
    min_duration = min(durations)
    max_duration = max(durations)
    assert min_duration == expected_min
    assert max_duration == expected_max

@pytest.mark.parametrize("expected_min_courses, expected_max_courses", [(['Python-разработчик с нуля'], ['Fullstack-разработчик на Python', 'Frontend-разработчик с нуля'])])
def test_min_max_courses(expected_min_courses, expected_max_courses):
    courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
    mentors = [
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    durations = [14, 20, 12, 20]

    courses_list = []
    for title, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": title, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    min_duration = min(durations)
    max_duration = max(durations)

    min_courses = []
    max_courses = []

    for course in courses_list:
        if course["duration"] == min_duration:
            min_courses.append(course["title"])
        if course["duration"] == max_duration:
            max_courses.append(course["title"])

    assert min_courses == expected_min_courses
    assert max_courses == expected_max_courses

@pytest.mark.parametrize("courses_list, expected_output", [
    ([
        {"title": "Java-разработчик с нуля", "mentors": ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"], "duration": 14},
        {"title": "Fullstack-разработчик на Python", "mentors": ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"], "duration": 20},
        {"title": "Python-разработчик с нуля", "mentors": ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"], "duration": 12},
        {"title": "Frontend-разработчик с нуля", "mentors": ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"], "duration": 20}
    ], [
        "Python-разработчик с нуля - 12 месяцев",
        "Java-разработчик с нуля - 14 месяцев",
        "Fullstack-разработчик на Python - 20 месяцев",
        "Frontend-разработчик с нуля - 20 месяцев"
    ])
])
def test_sorted_courses(courses_list, expected_output):
    output = []
    durations_dict = {}
    for id, course in enumerate(courses_list):
        duration = course["duration"]
        if duration in durations_dict:
            durations_dict[duration].append(id)
        else:
            durations_dict[duration] = [id]
    durations_dict = dict(sorted(durations_dict.items()))
    for duration, course_ids in durations_dict.items():
        for id in course_ids:
            course = courses_list[id]
            output.append(f'{course["title"]} - {duration} месяцев')
    assert output == expected_output

