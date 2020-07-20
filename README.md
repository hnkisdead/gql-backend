# Демо graphql в django

## GraphQL
Основы GraphQL [ссылка][1], [ссылка][2], [ссылка][3]

Анатомия запроса GraphQL [ссылка][4]

Graphene и Graphene Django [ссылка][5], [ссылка][6]

Работа с ошибками [ссылка][7]

Правила написания схем [ссылка][8], [ссылка][9]

Про архитектуру Relay [ссылка][10]

## Авторизация
В каждый резолвер и мутацию приходит аргумент info в котором есть context который по сути request из django

Много про авторизацию есть в этом видео [ссылка][11]

## Пагинация
Сделано

Способы описывать пагинацию [ссылка][12], [ссылка][13]

## Сортировки и фильтрация
Сделано

Как описывать схему для фильтров и сортировок [ссылка][14]

## Производительность 
Для сокращения запросов есть история с даталоадерами [ссылка][15], [ссылка][16], [ссылка][17]

Для защиты от сложных запросов есть несколько разных подходов [ссылка][18]

## Фикстуры
Сделано
 
## Разбиение на пакеты и модули
Сделано

## Документация типам схемы
Сделано

## Elasticsearch
В процессе

## Тесты
В процессе

## Генерация типов для фронтенда
Как генерировать правильно типы для фронтенда для разных релизов, новых веток, etc?

## CI/CD
Репортер схемы в репозиторий схем??? [ссылка][19]

## Метрики
Что делать с newrelic, sentry, etc?

## Обработка ошибок
Как лучше возвращать ошибки? [ссылка][21] [ссылка][22] [ссылка][23]

Ошибки в Apollo Server [ссылка][20]

[1]: https://www.apollographql.com/blog/the-basics-of-graphql-in-5-links-9e1dc4cac055/
[2]: https://www.apollographql.com/blog/graphql-explained-5844742f195e/
[3]: https://www.youtube.com/watch?v=F4vHSHzpO1g
[4]: https://www.apollographql.com/blog/the-anatomy-of-a-graphql-query-6dffa9e9e747/
[5]: https://docs.graphene-python.org/en/latest/types/schema/ 
[6]: https://docs.graphene-python.org/projelcts/django/en/latest/installation/
[7]: https://www.apollographql.com/blog/full-stack-error-handling-with-graphql-apollo-5c12da407210/
[8]: https://github.com/nodkz/graphql-rules-ru/tree/master/docs
[9]: https://www.youtube.com/watch?v=tASEYJXdO_c
[10]: https://www.apollographql.com/blog/explaining-graphql-connections-c48b7c3d6976/
[11]: https://www.youtube.com/watch?v=NnnvOPdstzg&t=1892s
[12]: https://www.apollographql.com/blog/understanding-pagination-rest-graphql-and-relay-b10f835549e7/
[13]: https://github.com/nodkz/graphql-rules-ru/blob/master/docs/05-list/5.4-pagination.md
[14]: https://www.youtube.com/watch?v=dDxUu-K2qdE
[15]: https://www.youtube.com/watch?v=NnnvOPdstzg&t=1892s
[16]: https://apirobot.me/posts/django-graphql-solving-n-1-problem-using-dataloaders
[17]: https://blog.logrocket.com/designing-graphql-server-optimal-performance/
[18]: https://www.apollographql.com/blog/securing-your-graphql-api-from-malicious-queries-16130a324a6b/
[19]: https://www.apollographql.com/blog/track-schema-changes-with-apollo-schema-reporting/
[20]: https://www.apollographql.com/blog/full-stack-error-handling-with-graphql-apollo-5c12da407210/
[21]: https://github.com/nodkz/graphql-rules-ru/blob/master/docs/06-mutations/6.6.4-payload-errors.md
[22]: https://www.facebook.com/MoscowGraphql/videos/206572663566137/
[23]: https://github.com/nodkz/conf-talks/tree/master/articles/graphql/errors