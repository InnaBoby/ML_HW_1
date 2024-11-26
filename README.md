# ML_HW_1
Home work 1 : regression with inference

## **Docs:**

- **AI_HW1_Regression_with_inference_pro.ipynb** - ноутбук с EDA, моделью регрессии и проведёнными экспериментами
- **Lasso.pkl** -  файл с весами лучшей модели (Лассо регрессия, кастомный feature engineering, параметры скейлинга и импьютера)
- **castom_transform.py** - файл с функцией для генерации новых признаков
- **SalesAuto_report.html** - отчет data_profiler
- **main.py** - файл с попыткой реализовать сервис
- **README.md** - файл с основнями выводами

## **Основные выводы:**

**Что было сделано:**

- предобработаны дефекты датасета, такие как дубликаты, пропуски, неверный формат колонок, непригодный формат значений,
- проведен разведочный анализ данных, а также взаимоствязь признаков между сосбой и с целевой переменной,
- визуализация,
- построена базовая модель регрессии
- проведены эксперименты по улучшению качества модели, включающие подбор гиперпараметров с использованием GridSearchCV, генерацию новых признаков, кодирование категориальных признаков


**Результаты:**
 - Удалось улучшить качество модели с метрики R2=-1.01 до R2=0.54
 - Наибольший прирост по качеству дало применение модели Лассо с подобранными GridSearchCV оптимальными параметрами и кастомная генерация признаков


**Что не получилось:**
-не получилось запустить сервер (из-за проблем с загрузкой кастомной функции)
