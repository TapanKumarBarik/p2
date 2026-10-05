# OpenSearch: From Zero to a Hands-On Search Project

> A practical learning path for understanding OpenSearch, running it locally with Docker, learning the core APIs and search features, and building a small production-style application.

**Goal:** By the end of this guide you should be able to explain OpenSearch, run a local cluster, create indexes and mappings, ingest data, write useful queries, build aggregations, use OpenSearch Dashboards, understand relevance and analyzers, and build a Python API on top of OpenSearch.

---

## 0. What You Will Build

We will build a small **Product Search Engine**.

Think of an e-commerce search box:

```text
User
  |
  v
FastAPI
  |
  +----> OpenSearch
  |        |
  |        +-- Full-text search
  |        +-- Filters
  |        +-- Sorting
  |        +-- Facets / aggregations
  |        +-- Autocomplete
  |        +-- Relevance ranking
  |        +-- Geo search
  |        +-- Optional vector / semantic search
  |
  v
JSON response
```

Example:

```text
GET /products/search?q=wireless+headphones&category=audio&min_price=1000&max_price=10000
```

OpenSearch should return the most relevant products, not simply products whose title happens to contain the exact words.

---

# 1. What Is OpenSearch?

OpenSearch is a distributed search and analytics engine built on Apache Lucene.

It can be used for:

- Full-text search
- Product search
- Log analytics
- Observability
- Security analytics
- Metrics and traces
- Analytics and aggregations
- Vector / semantic search
- AI-powered search applications

The official documentation describes OpenSearch as both a search and analytics engine and a vector database. It is commonly paired with:

- **OpenSearch Dashboards** for visualization and exploration
- **Data Prepper** for ingestion and transformation
- **Language clients** for application integration

Useful mental model:

```text
PostgreSQL
    |
    +-- excellent transactional database
    +-- joins
    +-- constraints
    +-- normalized data

OpenSearch
    |
    +-- excellent search
    +-- relevance
    +-- text analysis
    +-- aggregations
    +-- distributed search
    +-- vectors
```

OpenSearch is not a replacement for every database.

A common architecture is:

```text
Application
    |
    +------------------> PostgreSQL
    |                      |
    |                      +-- source of truth
    |
    +------------------> OpenSearch
                           |
                           +-- searchable projection
```

---

# 2. OpenSearch vs Elasticsearch

OpenSearch and Elasticsearch share a large amount of historical DNA and many concepts are similar.

At a high level:

| Concept | OpenSearch |
|---|---|
| Search engine | Yes |
| Lucene based | Yes |
| JSON REST API | Yes |
| Distributed | Yes |
| Full-text search | Yes |
| Aggregations | Yes |
| Dashboards | Yes |
| Vector search | Yes |
| Python client | Yes |
| SQL/PPL capabilities | Yes |
| Log/observability use cases | Yes |

If you already understand Elasticsearch terminology, a lot of the underlying mental model transfers.

However, always check the OpenSearch documentation for the exact syntax and feature support of the version you are running.

---

# 3. The Mental Model You Must Understand

The most important concepts are:

```text
Cluster
  |
  +-- Nodes
       |
       +-- Index
            |
            +-- Shards
            |     |
            |     +-- Documents
            |
            +-- Mappings
            |
            +-- Settings
            |
            +-- Aliases
```

Let's unpack that.

---

## 3.1 Cluster

A cluster is a collection of OpenSearch nodes working together.

Example:

```text
OpenSearch Cluster

+---------------------+
| Cluster              |
|                      |
|  Node 1              |
|  Node 2              |
|  Node 3              |
+---------------------+
```

For local learning you can start with one node.

For production, multiple nodes are common.

---

## 3.2 Node

A node is one running OpenSearch instance.

Example:

```text
Cluster
|
+-- node-1
+-- node-2
+-- node-3
```

Nodes can have different responsibilities depending on configuration and deployment architecture.

---

## 3.3 Index

An index is a logical collection of documents.

For example:

```text
products
```

could contain:

```json
{
  "id": 101,
  "name": "Sony Wireless Headphones",
  "category": "audio",
  "price": 7999
}
```

Think:

```text
Database table  ~  OpenSearch index
Row             ~  Document
Column          ~  Field
```

This analogy is useful, but not exact.

---

## 3.4 Document

A document is a JSON object stored in an index.

Example:

```json
{
  "product_id": "P1001",
  "name": "Wireless Noise Cancelling Headphones",
  "category": "audio",
  "brand": "Sony",
  "price": 12999,
  "rating": 4.6,
  "stock": 42
}
```

---

## 3.5 Field

A field is a property inside a document.

```json
{
  "name": "Headphones",
  "price": 9999
}
```

Fields:

```text
name
price
```

---

## 3.6 Mapping

A mapping describes how fields should be interpreted.

Example:

```json
{
  "mappings": {
    "properties": {
      "name": {
        "type": "text"
      },
      "price": {
        "type": "float"
      },
      "category": {
        "type": "keyword"
      }
    }
  }
}
```

Mapping is extremely important.

It determines whether a field behaves like:

```text
text
keyword
integer
long
float
double
boolean
date
geo_point
nested
object
vector-related types
```

---

# 4. `text` vs `keyword`

This is one of the most important OpenSearch concepts.

## `text`

Used for full-text search.

Example:

```json
"name": {
  "type": "text"
}
```

Good for:

```text
wireless headphones
noise cancelling headphones
best gaming keyboard
```

The text is analyzed.

---

## `keyword`

Used for exact values, filtering, grouping, sorting, and aggregations.

Example:

```json
"category": {
  "type": "keyword"
}
```

Good for:

```text
audio
laptop
mobile
gaming
```

You usually do not want to analyze a category into individual words.

---

## Common pattern

For a product name:

```json
"name": {
  "type": "text",
  "fields": {
    "keyword": {
      "type": "keyword"
    }
  }
}
```

Now you can have:

```text
name
    |
    +-- text
    |
    +-- name.keyword
```

Use:

```text
name
```

for full-text search.

Use:

```text
name.keyword
```

for exact sorting/aggregation where appropriate.

---

# 5. Shards and Replicas

This is another concept you absolutely need.

Suppose:

```text
products
```

contains 100 million documents.

You don't want one giant physical structure.

OpenSearch can divide the index into shards.

```text
products index

+------------------+
| shard 0          |
+------------------+

+------------------+
| shard 1          |
+------------------+

+------------------+
| shard 2          |
+------------------+

+------------------+
| shard 3          |
+------------------+
```

A shard is a Lucene index.

---

## Replicas

Replicas provide additional copies of shards.

Example:

```text
Primary shard 0
      |
      +---- Replica shard 0
```

Benefits include:

- Fault tolerance
- Additional search capacity

But replicas consume storage and resources.

---

## Important mental model

```text
Index
 |
 +-- Primary shard
 |
 +-- Primary shard
 |
 +-- Replica
 |
 +-- Replica
```

Don't blindly increase shard count.

Too many shards can hurt performance and operational simplicity.

---

# 6. How Search Actually Works

When you send:

```json
{
  "query": {
    "match": {
      "name": "wireless headphones"
    }
  }
}
```

OpenSearch does not simply perform:

```python
if "wireless headphones" in name:
```

Instead, text is analyzed and indexed.

A simplified pipeline:

```text
"Wireless Noise Cancelling Headphones"
                  |
                  v
             Analyzer
                  |
                  v
      ["wireless", "noise",
       "cancelling", "headphones"]
                  |
                  v
             Inverted Index
```

The inverted index is one of the fundamental structures behind fast text search.

---

# 7. Analyzer

An analyzer converts text into searchable terms.

It can contain:

```text
Character filters
       |
       v
Tokenizer
       |
       v
Token filters
       |
       v
Tokens
```

Example:

```text
"The Quick Brown Fox"
```

could become:

```text
the
quick
brown
fox
```

depending on the analyzer.

---

# 8. Tokenizer

A tokenizer breaks text into tokens.

Conceptually:

```text
"wireless headphones"

        |
        v

["wireless", "headphones"]
```

---

# 9. Token Filters

Token filters modify tokens.

Examples:

- Lowercase
- Stop words
- Stemming
- Synonyms

Example:

```text
"Running"
```

could be normalized/stemmed depending on configuration.

---

# 10. BM25 and Relevance

Search engines need to decide:

> Which document should appear first?

OpenSearch uses relevance scoring mechanisms based on Lucene.

A commonly encountered similarity is BM25.

Simplified idea:

```text
Query:
"wireless headphones"

Document A:
"Wireless Noise Cancelling Headphones"

Document B:
"Phone case"
```

Document A should score higher.

Factors include things such as:

- Term frequency
- Inverse document frequency
- Field length

You do not need to memorize the BM25 equation initially.

Understand the principle:

```text
matching query terms
        +
importance of those terms
        +
document characteristics
        =
relevance score
```

---

# 11. Install OpenSearch Locally

## Prerequisites

Install:

- Docker
- Docker Compose

Docker Desktop includes Docker Compose on typical desktop installations.

OpenSearch documentation recommends at least around 4 GB of Docker Desktop memory for local deployments.

---

# 12. Fastest Local Setup

For a quick throwaway test environment, OpenSearch can be started with security disabled.

Example:

```bash
docker pull opensearchproject/opensearch:latest

docker run -d \
  -p 9200:9200 \
  -p 9600:9600 \
  -e "discovery.type=single-node" \
  -e "DISABLE_SECURITY_PLUGIN=true" \
  --name opensearch \
  opensearchproject/opensearch:latest
```

Then:

```bash
curl http://localhost:9200
```

This is for local testing only.

Do not expose an unsecured instance to the public internet.

---

# 13. Recommended Docker Compose Setup

Create:

```text
opensearch-learning/
│
├── docker-compose.yml
├── .env
├── data/
└── project/
```

For learning, a single-node development environment is easiest.

Example:

```yaml
services:
  opensearch:
    image: opensearchproject/opensearch:latest
    container_name: opensearch
    environment:
      - discovery.type=single-node
      - DISABLE_SECURITY_PLUGIN=true
      - "OPENSEARCH_JAVA_OPTS=-Xms512m -Xmx512m"
    ports:
      - "9200:9200"
      - "9600:9600"
    volumes:
      - opensearch-data:/usr/share/opensearch/data

  dashboards:
    image: opensearchproject/opensearch-dashboards:latest
    container_name: opensearch-dashboards
    environment:
      - 'OPENSEARCH_HOSTS=["http://opensearch:9200"]'
      - DISABLE_SECURITY_DASHBOARDS_PLUGIN=true
    ports:
      - "5601:5601"
    depends_on:
      - opensearch

volumes:
  opensearch-data:
```

Start:

```bash
docker compose up -d
```

Check:

```bash
docker compose ps
```

Logs:

```bash
docker compose logs opensearch
```

Stop:

```bash
docker compose down
```

Stop and delete data:

```bash
docker compose down -v
```

---

# 14. OpenSearch URLs

OpenSearch API:

```text
http://localhost:9200
```

OpenSearch Dashboards:

```text
http://localhost:5601
```

Performance analyzer port:

```text
9600
```

---

# 15. First Health Checks

Run:

```bash
curl http://localhost:9200
```

Cluster health:

```bash
curl http://localhost:9200/_cluster/health
```

Pretty JSON:

```bash
curl "http://localhost:9200/_cluster/health?pretty"
```

Cluster state:

```bash
curl "http://localhost:9200/_cluster/state?pretty"
```

Nodes:

```bash
curl "http://localhost:9200/_cat/nodes?v"
```

Indexes:

```bash
curl "http://localhost:9200/_cat/indices?v"
```

---

# 16. OpenSearch Dashboards

Open:

```text
http://localhost:5601
```

One of the most useful areas while learning is **Dev Tools**.

It lets you run API calls without leaving the browser.

Example:

```http
GET _cluster/health
```

Then:

```http
GET _cat/indices?v
```

Then:

```http
GET products/_search
{
  "query": {
    "match_all": {}
  }
}
```

For learning, keep Dashboards open almost permanently.

---

# 17. Your First Index

Create:

```http
PUT products
```

Check:

```http
GET _cat/indices?v
```

Delete:

```http
DELETE products
```

---

# 18. Create an Index with Mapping

Use an explicit mapping.

```http
PUT products
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  },
  "mappings": {
    "properties": {
      "product_id": {
        "type": "keyword"
      },
      "name": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword"
          }
        }
      },
      "description": {
        "type": "text"
      },
      "brand": {
        "type": "keyword"
      },
      "category": {
        "type": "keyword"
      },
      "price": {
        "type": "float"
      },
      "rating": {
        "type": "float"
      },
      "stock": {
        "type": "integer"
      },
      "created_at": {
        "type": "date"
      }
    }
  }
}
```

---

# 19. Index a Document

```http
PUT products/_doc/P1001
{
  "product_id": "P1001",
  "name": "Wireless Noise Cancelling Headphones",
  "description": "Premium wireless headphones with active noise cancellation.",
  "brand": "Sony",
  "category": "audio",
  "price": 12999,
  "rating": 4.6,
  "stock": 42,
  "created_at": "2026-10-01"
}
```

Retrieve it:

```http
GET products/_doc/P1001
```

---

# 20. Generate an ID Automatically

```http
POST products/_doc
{
  "product_id": "P1002",
  "name": "Mechanical Gaming Keyboard",
  "description": "RGB mechanical keyboard for gaming and programming.",
  "brand": "Keychron",
  "category": "keyboard",
  "price": 8999,
  "rating": 4.7,
  "stock": 25,
  "created_at": "2026-10-01"
}
```

---

# 21. Update a Document

```http
POST products/_update/P1001
{
  "doc": {
    "price": 11999,
    "stock": 50
  }
}
```

---

# 22. Delete a Document

```http
DELETE products/_doc/P1001
```

---

# 23. Match All

```http
GET products/_search
{
  "query": {
    "match_all": {}
  }
}
```

---

# 24. Basic Full-Text Search

```http
GET products/_search
{
  "query": {
    "match": {
      "name": "wireless headphones"
    }
  }
}
```

This is a full-text query.

The `name` field is analyzed.

---

# 25. Exact Matching

For exact values:

```http
GET products/_search
{
  "query": {
    "term": {
      "brand": "Sony"
    }
  }
}
```

Use `term` for exact-value style queries.

For analyzed text, prefer appropriate full-text queries such as `match`.

---

# 26. Match Phrase

```http
GET products/_search
{
  "query": {
    "match_phrase": {
      "name": "noise cancelling headphones"
    }
  }
}
```

Phrase search cares about the order and proximity of terms.

---

# 27. Boolean Query

Combine conditions:

```http
GET products/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "name": "wireless headphones"
          }
        }
      ],
      "filter": [
        {
          "term": {
            "brand": "Sony"
          }
        },
        {
          "range": {
            "price": {
              "lte": 20000
            }
          }
        }
      ]
    }
  }
}
```

Mental model:

```text
must
  -> contributes to relevance

filter
  -> restricts results
  -> normally does not affect relevance
```

This distinction is extremely useful.

---

# 28. `must`

```json
{
  "must": [
    {
      "match": {
        "name": "gaming keyboard"
      }
    }
  ]
}
```

Documents need to satisfy the clause.

---

# 29. `should`

```json
{
  "should": [
    {
      "match": {
        "name": "wireless"
      }
    },
    {
      "match": {
        "description": "bluetooth"
      }
    }
  ]
}
```

Useful for boosting relevance.

---

# 30. `must_not`

```json
{
  "must_not": [
    {
      "term": {
        "brand": "UnknownBrand"
      }
    }
  ]
}
```

Excludes matching documents.

---

# 31. `filter`

Filters are ideal for:

- Price
- Category
- Brand
- Availability
- Date ranges
- Boolean flags

Example:

```http
GET products/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "price": {
              "gte": 5000,
              "lte": 15000
            }
          }
        },
        {
          "term": {
            "category": "audio"
          }
        }
      ]
    }
  }
}
```

---

# 32. Range Queries

```http
GET products/_search
{
  "query": {
    "range": {
      "price": {
        "gte": 5000,
        "lte": 20000
      }
    }
  }
}
```

Date example:

```http
GET products/_search
{
  "query": {
    "range": {
      "created_at": {
        "gte": "2026-01-01",
        "lte": "2026-12-31"
      }
    }
  }
}
```

---

# 33. Exists Query

```http
GET products/_search
{
  "query": {
    "exists": {
      "field": "stock"
    }
  }
}
```

---

# 34. Prefix Query

```http
GET products/_search
{
  "query": {
    "prefix": {
      "name": "wire"
    }
  }
}
```

Prefix queries should be used thoughtfully because some wildcard-style searches can become expensive.

---

# 35. Wildcard Query

```http
GET products/_search
{
  "query": {
    "wildcard": {
      "name.keyword": "*phone*"
    }
  }
}
```

Do not make wildcard queries your default search strategy.

---

# 36. Fuzzy Search

Useful when users make spelling mistakes.

```http
GET products/_search
{
  "query": {
    "match": {
      "name": {
        "query": "headphons",
        "fuzziness": "AUTO"
      }
    }
  }
}
```

---

# 37. Query String

Example:

```http
GET products/_search
{
  "query": {
    "query_string": {
      "query": "wireless AND headphones"
    }
  }
}
```

Useful when you intentionally want query-string syntax.

Do not blindly expose arbitrary user input to advanced query syntax without understanding the implications.

---

# 38. Search Specific Fields

```http
GET products/_search
{
  "query": {
    "multi_match": {
      "query": "wireless headphones",
      "fields": [
        "name^3",
        "description",
        "brand"
      ]
    }
  }
}
```

The `^3` means:

```text
name is boosted
```

So matching the name is more important.

---

# 39. Search with Boosting

Example:

```json
{
  "multi_match": {
    "query": "gaming keyboard",
    "fields": [
      "name^5",
      "brand^2",
      "description"
    ]
  }
}
```

Think:

```text
name          x5 importance
brand         x2 importance
description   x1 importance
```

This is one of the first techniques you should learn for building useful product search.

---

# 40. Sorting

Sort by price:

```http
GET products/_search
{
  "query": {
    "match_all": {}
  },
  "sort": [
    {
      "price": {
        "order": "asc"
      }
    }
  ]
}
```

Sort by rating:

```json
"sort": [
  {
    "rating": {
      "order": "desc"
    }
  }
]
```

---

# 41. Pagination

Simple pagination:

```http
GET products/_search
{
  "from": 0,
  "size": 10,
  "query": {
    "match_all": {}
  }
}
```

Page 2:

```json
{
  "from": 10,
  "size": 10
}
```

But deep pagination can become expensive.

For large result sets, learn:

- `search_after`
- Point-in-time techniques where supported
- Scroll for appropriate bulk-processing use cases

---

# 42. Search After

Conceptually:

```text
Page 1
   |
   +-- last sort values
            |
            v
Page 2
```

Example:

```http
GET products/_search
{
  "size": 10,
  "query": {
    "match_all": {}
  },
  "sort": [
    {
      "price": "asc"
    },
    {
      "_id": "asc"
    }
  ],
  "search_after": [
    9999,
    "P1020"
  ]
}
```

The exact sort values come from the previous response.

---

# 43. Aggregations

Aggregations let you analyze data.

Example:

```http
GET products/_search
{
  "size": 0,
  "aggs": {
    "categories": {
      "terms": {
        "field": "category"
      }
    }
  }
}
```

Possible result:

```text
audio      120
laptop      80
keyboard    50
mobile      40
```

---

# 44. Why Aggregations Matter

A product search page might show:

```text
Results: 2,340

Category
[ ] Audio       430
[ ] Laptop      300
[ ] Keyboard    210

Brand
[ ] Sony        100
[ ] Dell         90
[ ] HP           80

Price
₹0 - ₹5,000
₹5,000 - ₹10,000
₹10,000+
```

These are often powered by aggregations.

---

# 45. Average

```http
GET products/_search
{
  "size": 0,
  "aggs": {
    "average_price": {
      "avg": {
        "field": "price"
      }
    }
  }
}
```

---

# 46. Min / Max

```http
GET products/_search
{
  "size": 0,
  "aggs": {
    "max_price": {
      "max": {
        "field": "price"
      }
    },
    "min_price": {
      "min": {
        "field": "price"
      }
    }
  }
}
```

---

# 47. Histogram

```http
GET products/_search
{
  "size": 0,
  "aggs": {
    "price_ranges": {
      "histogram": {
        "field": "price",
        "interval": 5000
      }
    }
  }
}
```

---

# 48. Nested Aggregations

You can combine aggregations.

```http
GET products/_search
{
  "size": 0,
  "aggs": {
    "categories": {
      "terms": {
        "field": "category"
      },
      "aggs": {
        "average_price": {
          "avg": {
            "field": "price"
          }
        }
      }
    }
  }
}
```

---

# 49. Faceted Search

A classic search architecture:

```text
                 Search
                   |
          +--------+--------+
          |                 |
       Results          Aggregations
                           |
              +------------+------------+
              |            |            |
           Category       Brand        Price
```

This is called faceted search.

Your project will implement this.

---

# 50. Explain Why a Document Matched

Use:

```http
GET products/_search
{
  "explain": true,
  "query": {
    "match": {
      "name": "wireless headphones"
    }
  }
}
```

This is useful when learning relevance.

It can help answer:

> Why did product A rank above product B?

Use it for debugging rather than normal production requests.

---

# 51. `_source`

By default, search responses can include the original document.

You can restrict fields:

```http
GET products/_search
{
  "_source": [
    "product_id",
    "name",
    "price",
    "rating"
  ],
  "query": {
    "match": {
      "name": "headphones"
    }
  }
}
```

---

# 52. Bulk API

Never send thousands of documents with thousands of individual HTTP requests if you can batch them appropriately.

Bulk format:

```http
POST _bulk
{"index":{"_index":"products","_id":"P1"}}
{"product_id":"P1","name":"Laptop","category":"laptop","price":50000}
{"index":{"_index":"products","_id":"P2"}}
{"product_id":"P2","name":"Keyboard","category":"keyboard","price":5000}
```

Important:

The bulk API uses newline-delimited JSON.

The request must end with a newline.

---

# 53. Refresh

When you index a document, there can be a short delay before it becomes searchable.

This is related to refresh behavior.

Conceptually:

```text
Application
    |
    v
Index document
    |
    v
Lucene structures
    |
    v
Refresh
    |
    v
Searchable
```

Do not force refresh after every write in a high-throughput system unless you have a specific reason.

---

# 54. Segments

Lucene stores indexed data in segments.

Simplified:

```text
Shard
 |
 +-- segment 1
 +-- segment 2
 +-- segment 3
 +-- segment 4
```

Segments are immutable.

Background merging combines smaller segments.

This is one reason OpenSearch performance can behave differently from a traditional OLTP database.

---

# 55. Delete Is Not Always Physically Instant

A delete/update can result in old data being marked as deleted and eventually reclaimed during segment merging.

This matters when thinking about:

- Storage
- Segment counts
- Merge behavior
- Performance

You don't need to manage this manually at first.

Just understand the architecture.

---

# 56. Index Templates

Suppose you create many indexes:

```text
logs-2026.10.01
logs-2026.10.02
logs-2026.10.03
```

You don't want to manually define mappings every day.

An index template can apply settings and mappings automatically.

Conceptually:

```text
Template
   |
   +-- logs-*
         |
         +-- settings
         +-- mappings
```

Example:

```http
PUT _index_template/products_template
{
  "index_patterns": [
    "products-*"
  ],
  "template": {
    "settings": {
      "number_of_shards": 1
    },
    "mappings": {
      "properties": {
        "name": {
          "type": "text"
        },
        "category": {
          "type": "keyword"
        }
      }
    }
  }
}
```

---

# 57. Aliases

Aliases are logical names pointing to indexes.

Example:

```text
products
   |
   +-- products-v1
```

Later:

```text
products
   |
   +-- products-v2
```

This enables safer index migrations.

Conceptually:

```text
products alias
      |
      v
products-v2
```

Application code does not need to know the physical index version.

---

# 58. Index Versioning Pattern

Useful deployment pattern:

```text
products-v1
products-v2

       |
       v

products alias
```

Migration:

```text
1. Create v2
2. Populate v2
3. Validate v2
4. Switch alias
5. Remove v1 later
```

This is much safer than mutating critical mappings in place.

---

# 59. Object vs Nested

Consider:

```json
{
  "employees": [
    {
      "name": "Alice",
      "skills": ["Python", "AI"]
    },
    {
      "name": "Bob",
      "skills": ["Java", "AWS"]
    }
  ]
}
```

Arrays of objects can create surprising matching behavior when represented as normal objects.

`nested` is useful when each object must maintain its own relationship between fields.

Example:

```json
"employees": {
  "type": "nested"
}
```

Learn this carefully before designing complex schemas.

---

# 60. Geo Search

OpenSearch supports geo-related use cases.

Example field:

```json
"location": {
  "type": "geo_point"
}
```

Document:

```json
{
  "name": "Store A",
  "location": {
    "lat": 12.9716,
    "lon": 77.5946
  }
}
```

You can then search by distance.

Example concept:

```text
Find stores
within 10 km
of a location
```

This is useful for:

- Store locators
- Delivery
- Nearby services
- Location-aware search

---

# 61. Date Search

Dates should normally have a date mapping.

Example:

```json
"created_at": {
  "type": "date"
}
```

Then:

```http
GET products/_search
{
  "query": {
    "range": {
      "created_at": {
        "gte": "now-30d/d"
      }
    }
  }
}
```

---

# 62. Autocomplete

A real search box needs autocomplete.

Possible approaches include:

- Prefix queries
- Edge n-grams
- Search-as-you-type style mappings where supported
- Completion-oriented structures
- Dedicated autocomplete indexes

For a beginner project, start with a simple prefix/autocomplete strategy.

Then learn edge n-grams.

---

# 63. Edge N-Gram Concept

Input:

```text
headphones
```

Could produce:

```text
h
he
hea
head
headp
headph
...
```

Then:

```text
hea
```

can match:

```text
headphones
```

This can power search-as-you-type behavior.

However, n-grams increase index size, so use them deliberately.

---

# 64. Custom Analyzer

Conceptually:

```json
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase"
          ]
        }
      }
    }
  }
}
```

Then map a field to it:

```json
"name": {
  "type": "text",
  "analyzer": "my_analyzer"
}
```

---

# 65. Test an Analyzer

A very useful learning API:

```http
POST _analyze
{
  "analyzer": "standard",
  "text": "Wireless Noise Cancelling Headphones"
}
```

Study the tokens.

This is one of the best ways to understand why a search behaves the way it does.

---

# 66. Search Relevance Strategy

A good product search often combines:

```text
Exact match
    +
Phrase match
    +
Full-text match
    +
Field boosting
    +
Business signals
    +
Filters
```

For example:

```text
name exact match       high importance
name phrase match     high importance
brand match            medium importance
description match      lower importance
rating                 business signal
stock                  business rule
```

Do not rely on one query type for every search experience.

---

# 67. Business Ranking

Suppose two products both match:

```text
wireless headphones
```

You may prefer:

```text
rating 4.8
stock 100
```

over:

```text
rating 3.5
stock 2
```

Search relevance and business relevance are different dimensions.

A mature search engine combines both.

---

# 68. OpenSearch SQL

OpenSearch also provides SQL capabilities.

Conceptually:

```sql
SELECT category, AVG(price)
FROM products
GROUP BY category;
```

This can be useful for analytics users who prefer SQL.

For learning, start with Query DSL first.

Then explore SQL.

---

# 69. PPL

OpenSearch also provides Piped Processing Language (PPL) for data exploration and analytics workflows.

A useful learning progression is:

```text
Query DSL
    |
    v
Aggregations
    |
    v
SQL
    |
    v
PPL
```

---

# 70. OpenSearch Dashboards

Dashboards can be used for:

- Data exploration
- Visualizations
- Search
- Monitoring
- Logs
- Analytics
- Query experimentation

Use it to build:

```text
Product Search Analytics

Total Products
Average Price
Average Rating

Products by Category
Products by Brand
Price Distribution
```

---

# 71. Security

Do not confuse:

```text
Local learning
```

with:

```text
Production deployment
```

For local experimentation, disabling the security plugin is convenient.

For production, you need to think about:

- Authentication
- Authorization
- TLS
- Certificates
- Roles
- Role mappings
- Network security
- Secrets
- Audit requirements
- Backup/recovery

OpenSearch's security plugin provides authentication and authorization capabilities.

---

# 72. Production Rule

Never do this:

```text
Public Internet
      |
      v
OpenSearch with security disabled
```

Instead:

```text
Internet
   |
   v
API Gateway / Application
   |
   v
Authenticated OpenSearch
```

---

# 73. Snapshots and Backups

Do not treat replicas as backups.

A replica protects against some node/shard failures.

A backup protects against things such as:

- Accidental deletion
- Data corruption
- Operational mistakes
- Disaster scenarios

Learn the snapshot/restore system before running production OpenSearch.

---

# 74. Monitoring

Important things to monitor include:

```text
Cluster health
Node health
CPU
Memory
JVM heap
Disk usage
Search latency
Indexing latency
Rejected requests
Shard health
Segment counts
Cache behavior
```

Useful APIs include:

```http
GET _cluster/health
GET _cat/nodes?v
GET _cat/indices?v
GET _cat/shards?v
GET _nodes/stats
```

---

# 75. Common Performance Mistakes

## Mistake 1: Too many shards

More shards does not automatically mean faster.

## Mistake 2: Huge documents

Keep documents reasonably sized.

## Mistake 3: Too many fields

Dynamic mapping can accidentally create enormous mappings.

## Mistake 4: Wildcard-heavy searches

Especially leading wildcards:

```text
*phone
```

can be expensive.

## Mistake 5: Refresh after every write

Can destroy indexing throughput.

## Mistake 6: Deep pagination

Prefer search-after style approaches for large result sets.

## Mistake 7: Aggregating on `text`

Use appropriate keyword/numeric/date fields.

## Mistake 8: Treating OpenSearch like PostgreSQL

Do not expect arbitrary joins and relational transactions.

---

# 76. The Project

We will now build:

# Product Search Engine

Technology:

```text
Python
FastAPI
OpenSearch
Docker
OpenSearch Dashboards
```

Optional later:

```text
Vector embeddings
Hybrid search
```

---

# 77. Project Structure

Create:

```text
opensearch-product-search/
│
├── docker-compose.yml
├── README.md
├── requirements.txt
│
├── data/
│   └── products.json
│
├── scripts/
│   ├── create_index.py
│   └── seed_data.py
│
└── app/
    ├── __init__.py
    ├── main.py
    ├── opensearch_client.py
    ├── schemas.py
    └── search.py
```

---

# 78. Python Dependencies

`requirements.txt`

```text
fastapi
uvicorn[standard]
opensearch-py
pydantic
```

Install:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Then:

```bash
pip install -r requirements.txt
```

---

# 79. OpenSearch Client

`app/opensearch_client.py`

```python
from opensearchpy import OpenSearch


client = OpenSearch(
    hosts=[
        {
            "host": "localhost",
            "port": 9200,
        }
    ],
    use_ssl=False,
    verify_certs=False,
)
```

Test:

```python
print(client.info())
```

---

# 80. Create the Index

`scripts/create_index.py`

```python
from opensearchpy import OpenSearch


client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    use_ssl=False,
    verify_certs=False,
)


INDEX = "products"


mapping = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
    },
    "mappings": {
        "properties": {
            "product_id": {
                "type": "keyword"
            },
            "name": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword"
                    }
                }
            },
            "description": {
                "type": "text"
            },
            "brand": {
                "type": "keyword"
            },
            "category": {
                "type": "keyword"
            },
            "price": {
                "type": "float"
            },
            "rating": {
                "type": "float"
            },
            "stock": {
                "type": "integer"
            },
            "created_at": {
                "type": "date"
            }
        }
    }
}


if client.indices.exists(index=INDEX):
    print(f"{INDEX} already exists")
else:
    client.indices.create(
        index=INDEX,
        body=mapping
    )
    print(f"Created {INDEX}")
```

Run:

```bash
python scripts/create_index.py
```

---

# 81. Sample Data

`data/products.json`

Use a dataset similar to:

```json
[
  {
    "product_id": "P1001",
    "name": "Sony Wireless Noise Cancelling Headphones",
    "description": "Premium wireless headphones with active noise cancellation.",
    "brand": "Sony",
    "category": "audio",
    "price": 12999,
    "rating": 4.6,
    "stock": 42,
    "created_at": "2026-09-01"
  },
  {
    "product_id": "P1002",
    "name": "Keychron Mechanical Gaming Keyboard",
    "description": "Mechanical RGB keyboard for gaming and programming.",
    "brand": "Keychron",
    "category": "keyboard",
    "price": 8999,
    "rating": 4.7,
    "stock": 25,
    "created_at": "2026-09-05"
  },
  {
    "product_id": "P1003",
    "name": "Dell 27 Inch 4K Monitor",
    "description": "4K monitor suitable for development and creative work.",
    "brand": "Dell",
    "category": "monitor",
    "price": 28999,
    "rating": 4.5,
    "stock": 18,
    "created_at": "2026-08-20"
  },
  {
    "product_id": "P1004",
    "name": "Apple Wireless Keyboard",
    "description": "Slim wireless keyboard for desktop productivity.",
    "brand": "Apple",
    "category": "keyboard",
    "price": 7499,
    "rating": 4.4,
    "stock": 32,
    "created_at": "2026-08-15"
  }
]
```

Add at least 30-50 products for meaningful aggregation experiments.

---

# 82. Seed Data

`scripts/seed_data.py`

```python
import json

from opensearchpy import OpenSearch, helpers


client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    use_ssl=False,
    verify_certs=False,
)

INDEX = "products"


with open("data/products.json", "r", encoding="utf-8") as file:
    products = json.load(file)


actions = []

for product in products:
    actions.append(
        {
            "_index": INDEX,
            "_id": product["product_id"],
            "_source": product,
        }
    )


success, failed = helpers.bulk(
    client,
    actions,
)

print("Indexed:", success)
print("Failed:", failed)
```

Run:

```bash
python scripts/seed_data.py
```

Verify:

```http
GET products/_count
```

Then:

```http
GET products/_search
{
  "query": {
    "match_all": {}
  }
}
```

---

# 83. Build the FastAPI API

`app/main.py`

```python
from fastapi import FastAPI, Query
from typing import Optional

from .opensearch_client import client


app = FastAPI(
    title="OpenSearch Product Search API"
)


@app.get("/health")
def health():
    return client.cluster.health()


@app.get("/products/search")
def search_products(
    q: str = Query(...),
    category: Optional[str] = None,
    brand: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    size: int = 10,
):
    filters = []

    if category:
        filters.append({
            "term": {
                "category": category
            }
        })

    if brand:
        filters.append({
            "term": {
                "brand": brand
            }
        })

    if min_price is not None or max_price is not None:
        range_query = {}

        if min_price is not None:
            range_query["gte"] = min_price

        if max_price is not None:
            range_query["lte"] = max_price

        filters.append({
            "range": {
                "price": range_query
            }
        })

    query = {
        "bool": {
            "must": [
                {
                    "multi_match": {
                        "query": q,
                        "fields": [
                            "name^4",
                            "brand^2",
                            "description"
                        ],
                        "fuzziness": "AUTO"
                    }
                }
            ],
            "filter": filters
        }
    }

    response = client.search(
        index="products",
        body={
            "size": size,
            "query": query,
        }
    )

    return response
```

Run:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

---

# 84. Test Your API

Search:

```text
http://localhost:8000/products/search?q=wireless%20headphones
```

With category:

```text
/products/search?q=keyboard&category=keyboard
```

With price:

```text
/products/search?q=keyboard&min_price=5000&max_price=10000
```

With brand:

```text
/products/search?q=wireless&brand=Sony
```

---

# 85. Improve the Search Response

Do not expose the entire raw OpenSearch response to your frontend forever.

Instead transform:

```text
OpenSearch response
       |
       v
Application service
       |
       v
Clean API response
```

Example target:

```json
{
  "query": "wireless headphones",
  "total": 12,
  "results": [
    {
      "id": "P1001",
      "name": "Sony Wireless Noise Cancelling Headphones",
      "brand": "Sony",
      "price": 12999,
      "rating": 4.6,
      "score": 7.82
    }
  ]
}
```

This separates your application contract from your search engine implementation.

---

# 86. Add Facets

Modify your search query:

```python
body = {
    "size": size,
    "query": query,
    "aggs": {
        "categories": {
            "terms": {
                "field": "category"
            }
        },
        "brands": {
            "terms": {
                "field": "brand"
            }
        },
        "price_stats": {
            "stats": {
                "field": "price"
            }
        }
    }
}
```

Now the response can power filters.

---

# 87. Target API Response

Eventually return:

```json
{
  "query": "wireless headphones",
  "total": 42,

  "results": [
    {
      "id": "P1001",
      "name": "Sony Wireless Noise Cancelling Headphones",
      "price": 12999,
      "rating": 4.6
    }
  ],

  "facets": {
    "categories": [
      {
        "key": "audio",
        "count": 31
      }
    ],
    "brands": [
      {
        "key": "Sony",
        "count": 12
      }
    ]
  }
}
```

Now you have a real search API.

---

# 88. Add Sorting

Support:

```text
relevance
price_low
price_high
rating
```

Example query:

```text
/products/search?q=headphones&sort=price_low
```

Build the OpenSearch sort dynamically.

Example:

```python
sort_map = {
    "price_low": [
        {"price": {"order": "asc"}}
    ],
    "price_high": [
        {"price": {"order": "desc"}}
    ],
    "rating": [
        {"rating": {"order": "desc"}}
    ]
}
```

For relevance, omit the explicit sort and let the relevance score determine ordering.

---

# 89. Add Pagination

API:

```text
/products/search?q=keyboard&page=2&size=10
```

For a first implementation:

```python
from_ = (page - 1) * size
```

Then:

```python
body = {
    "from": from_,
    "size": size,
    ...
}
```

Later replace deep pagination with search-after for large datasets.

---

# 90. Add Autocomplete

Create an endpoint:

```text
GET /products/autocomplete?q=wire
```

Start with a simple query:

```json
{
  "query": {
    "prefix": {
      "name.keyword": "wire"
    }
  }
}
```

Then improve it with a dedicated autocomplete mapping.

Challenge:

> Implement autocomplete that returns the top 10 suggestions in under a reasonable latency target on your local dataset.

---

# 91. Add Fuzzy Search

Try:

```text
headphons
```

The API should still find:

```text
headphones
```

Use:

```json
{
  "match": {
    "name": {
      "query": "headphons",
      "fuzziness": "AUTO"
    }
  }
}
```

---

# 92. Add Search Ranking

Create a ranking strategy:

```text
name match         x4
brand match        x2
description match  x1
```

Use:

```json
{
  "multi_match": {
    "query": "wireless headphones",
    "fields": [
      "name^4",
      "brand^2",
      "description"
    ]
  }
}
```

Experiment with:

```text
name^2
name^4
name^6
```

Observe how ranking changes.

---

# 93. Add Rating as a Business Signal

Now think beyond text relevance.

Suppose:

```text
Product A
relevance = 10
rating = 3.0

Product B
relevance = 9
rating = 4.9
```

Should B rank above A?

There is no universal answer.

You need a ranking strategy.

This is where search engineering becomes interesting.

---

# 94. Vector Search

Now enter modern AI search.

Traditional search:

```text
Query
 |
 v
Tokens
 |
 v
Keyword matching
 |
 v
Results
```

Semantic search:

```text
Query
 |
 v
Embedding
 |
 v
Vector similarity
 |
 v
Semantically similar documents
```

Example:

Query:

```text
headphones that block airplane noise
```

A semantic engine may understand that this relates to:

```text
active noise cancellation
```

even if those exact words don't appear in the query.

---

# 95. Vector Search Mental Model

Store:

```text
document
+
embedding vector
```

Example:

```json
{
  "name": "Noise Cancelling Headphones",
  "embedding": [0.012, -0.44, 0.83, ...]
}
```

Query:

```text
"headphones for noisy flights"
```

Generate:

```text
query embedding
```

Then find nearby vectors.

---

# 96. k-NN

k-NN means:

```text
k nearest neighbors
```

If:

```text
k = 10
```

you want the 10 most similar vectors.

OpenSearch supports vector search capabilities through its neural/vector search functionality.

Do not start your OpenSearch journey with vectors.

Learn:

```text
index
mapping
query
aggregation
relevance
```

first.

Then add vectors.

---

# 97. Hybrid Search

The most interesting modern architecture is often:

```text
                  Query
                    |
          +---------+---------+
          |                   |
          v                   v
     Keyword search      Vector search
          |                   |
          v                   v
       Results             Results
          |                   |
          +---------+---------+
                    |
                    v
              Combination
                    |
                    v
               Final rank
```

Why?

Keyword search is excellent for:

- Exact names
- Product IDs
- Brand names
- Specific terminology

Semantic search is excellent for:

- Meaning
- Paraphrases
- Natural language
- Conceptual similarity

Hybrid search combines the strengths.

---

# 98. Project Evolution

Your project can evolve like this:

### Version 1

```text
OpenSearch
+
CRUD
+
basic search
```

### Version 2

```text
FastAPI
+
filters
+
sorting
+
pagination
```

### Version 3

```text
aggregations
+
facets
+
autocomplete
+
fuzzy search
```

### Version 4

```text
custom analyzers
+
relevance tuning
+
business ranking
```

### Version 5

```text
embeddings
+
vector search
+
hybrid search
```

This gives you a strong progression from beginner to advanced.

---

# 99. Exercises

## Exercise 1

Create an index:

```text
books
```

Fields:

```text
title
author
genre
price
rating
published_at
```

---

## Exercise 2

Index 20 books.

---

## Exercise 3

Search:

```text
"machine learning"
```

using `match`.

---

## Exercise 4

Find books:

```text
price < 1000
```

---

## Exercise 5

Find:

```text
genre = technology
```

---

## Exercise 6

Sort by:

```text
rating DESC
```

---

## Exercise 7

Create aggregation:

```text
books per genre
```

---

## Exercise 8

Calculate:

```text
average book price
```

---

## Exercise 9

Implement:

```text
GET /books/search?q=...
```

---

## Exercise 10

Add:

```text
genre
min_price
max_price
```

filters.

---

# 100. Intermediate Challenges

## Challenge 1: Faceted Search

Return:

```text
results
+
genre counts
+
author counts
+
average price
```

---

## Challenge 2: Autocomplete

Implement:

```text
/books/autocomplete?q=mach
```

---

## Challenge 3: Typo Tolerance

Make:

```text
pythn
```

find:

```text
python
```

---

## Challenge 4: Ranking

Make title matches rank above description matches.

---

## Challenge 5: Pagination

Implement:

```text
page
size
```

Then investigate why deep pagination is problematic.

---

# 101. Advanced Challenges

## Challenge 6: Search After

Replace deep `from/size` pagination with `search_after`.

---

## Challenge 7: Alias Deployment

Create:

```text
products-v1
products-v2
```

and use:

```text
products
```

as an alias.

---

## Challenge 8: Custom Analyzer

Create an analyzer that:

```text
lowercases
+
normalizes text
```

Then inspect it using `_analyze`.

---

## Challenge 9: Geo Search

Add:

```text
store locations
```

and find stores within:

```text
5 km
```

---

## Challenge 10: Semantic Search

Add embeddings to your product descriptions.

Implement:

```text
query
  |
  v
embedding
  |
  v
k-NN
  |
  v
results
```

---

## Challenge 11: Hybrid Search

Combine:

```text
BM25-style lexical search
+
vector similarity
```

and compare results.

---

# 102. Useful APIs Cheat Sheet

## Cluster

```http
GET /
GET _cluster/health
GET _cluster/state
```

## Nodes

```http
GET _cat/nodes?v
GET _nodes/stats
```

## Indexes

```http
GET _cat/indices?v
PUT products
DELETE products
```

## Documents

```http
PUT products/_doc/1
GET products/_doc/1
POST products/_update/1
DELETE products/_doc/1
```

## Search

```http
GET products/_search
```

## Count

```http
GET products/_count
```

## Mapping

```http
GET products/_mapping
```

## Settings

```http
GET products/_settings
```

## Aliases

```http
GET _cat/aliases?v
```

## Shards

```http
GET _cat/shards?v
```

## Analyze

```http
POST _analyze
```

## Bulk

```http
POST _bulk
```

---

# 103. Query DSL Cheat Sheet

## Match

```json
{
  "match": {
    "name": "headphones"
  }
}
```

## Match phrase

```json
{
  "match_phrase": {
    "name": "noise cancelling headphones"
  }
}
```

## Term

```json
{
  "term": {
    "brand": "Sony"
  }
}
```

## Range

```json
{
  "range": {
    "price": {
      "gte": 5000,
      "lte": 15000
    }
  }
}
```

## Exists

```json
{
  "exists": {
    "field": "stock"
  }
}
```

## Boolean

```json
{
  "bool": {
    "must": [],
    "filter": [],
    "should": [],
    "must_not": []
  }
}
```

## Multi match

```json
{
  "multi_match": {
    "query": "wireless headphones",
    "fields": [
      "name^4",
      "description"
    ]
  }
}
```

---

# 104. Aggregation Cheat Sheet

## Terms

```json
{
  "terms": {
    "field": "category"
  }
}
```

## Average

```json
{
  "avg": {
    "field": "price"
  }
}
```

## Min

```json
{
  "min": {
    "field": "price"
  }
}
```

## Max

```json
{
  "max": {
    "field": "price"
  }
}
```

## Stats

```json
{
  "stats": {
    "field": "price"
  }
}
```

---

# 105. Debugging Checklist

When OpenSearch is not behaving as expected:

```text
1. Is the container running?
2. Is the cluster green/yellow/red?
3. Does the index exist?
4. What is the mapping?
5. Is the field text or keyword?
6. Is the query using the correct query type?
7. Are documents actually indexed?
8. Is the field analyzed?
9. What does _analyze produce?
10. What does explain say?
11. Are filters excluding results?
12. Is pagination hiding results?
13. Are shards healthy?
14. Is the query expensive?
15. Is the application sending the query you think it is?
```

---

# 106. The Most Important Debugging Commands

```http
GET _cluster/health
```

```http
GET _cat/indices?v
```

```http
GET products/_mapping
```

```http
GET products/_settings
```

```http
GET products/_count
```

```http
GET products/_search
{
  "query": {
    "match_all": {}
  }
}
```

```http
POST _analyze
{
  "analyzer": "standard",
  "text": "Wireless Noise Cancelling Headphones"
}
```

---

# 107. How to Think About OpenSearch in Real Systems

A typical enterprise architecture might look like:

```text
                 Users
                   |
                   v
              Frontend
                   |
                   v
             API Gateway
                   |
                   v
              Backend API
              /        \
             /          \
            v            v
       PostgreSQL     OpenSearch
       source data    search index
                         |
                         v
                    Dashboards
```

Data flow:

```text
Database
   |
   v
CDC / ETL / application events
   |
   v
Data Prepper / ingestion service
   |
   v
OpenSearch
```

For AI search:

```text
Documents
   |
   +------> lexical index
   |
   +------> embeddings
              |
              v
        vector index

Query
 |
 +------> lexical query
 |
 +------> embedding
             |
             v
          vector query
 |
 +---------+
 |
 v
hybrid ranking
 |
 v
results
```

---

# 108. OpenSearch vs PostgreSQL: When to Use Which

| Requirement | PostgreSQL | OpenSearch |
|---|---:|---:|
| Transactions | Excellent | Not primary purpose |
| Relational joins | Excellent | Limited/different model |
| Constraints | Excellent | Different model |
| Full-text search | Good | Excellent |
| Relevance ranking | Limited compared with search engines | Excellent |
| Faceted search | Possible | Excellent |
| Log analytics | Possible | Excellent |
| Vector search | Possible with extensions | Strong native ecosystem |
| Aggregations | Excellent | Excellent |
| Source of truth | Excellent | Usually not ideal |
| Search index | Not usually first choice | Excellent |

The common answer is not:

```text
PostgreSQL OR OpenSearch
```

It is often:

```text
PostgreSQL AND OpenSearch
```

---

# 109. Recommended Learning Order

Do not jump randomly between features.

Use this sequence.

## Level 1: Foundations

Learn:

```text
Cluster
Node
Index
Document
Field
Mapping
Shard
Replica
```

---

## Level 2: CRUD

Practice:

```text
Create index
Create document
Read document
Update document
Delete document
```

---

## Level 3: Search

Master:

```text
match
term
match_phrase
bool
filter
range
exists
multi_match
fuzzy
```

---

## Level 4: Search Engineering

Learn:

```text
analyzers
tokenizers
token filters
stemming
synonyms
boosting
relevance
BM25
explain
```

---

## Level 5: Analytics

Learn:

```text
terms
avg
min
max
stats
histogram
nested aggregations
facets
```

---

## Level 6: Operations

Learn:

```text
shards
replicas
refresh
segments
merges
aliases
templates
snapshots
monitoring
```

---

## Level 7: Application Development

Build:

```text
FastAPI
+
OpenSearch client
+
search
+
filters
+
facets
+
pagination
```

---

## Level 8: AI Search

Learn:

```text
embeddings
k-NN
vector search
semantic search
hybrid search
reranking
```

---

# 110. 14-Day Practical Learning Plan

## Day 1

Install Docker + OpenSearch.

Practice:

```text
GET /
GET _cluster/health
GET _cat/nodes?v
```

---

## Day 2

Learn:

```text
index
document
field
mapping
```

Create `products`.

---

## Day 3

CRUD.

Practice:

```text
PUT
GET
POST _update
DELETE
```

---

## Day 4

Search basics:

```text
match
term
match_phrase
```

---

## Day 5

Boolean search:

```text
must
filter
should
must_not
```

---

## Day 6

Range/filter/sort/pagination.

---

## Day 7

Aggregations.

Build:

```text
category facet
brand facet
price statistics
```

---

## Day 8

Analyzers.

Practice:

```http
POST _analyze
```

---

## Day 9

Relevance.

Learn:

```text
boosting
multi_match
explain
```

---

## Day 10

Build the FastAPI application.

---

## Day 11

Add:

```text
filters
sorting
pagination
facets
```

---

## Day 12

Add autocomplete and fuzzy search.

---

## Day 13

Learn:

```text
shards
replicas
aliases
templates
refresh
segments
```

---

## Day 14

Start vector search.

Then build hybrid search.

---

# 111. Final Project Requirements

Your finished project should support:

### Search

```text
GET /products/search?q=...
```

### Filters

```text
category
brand
min_price
max_price
rating
in_stock
```

### Sorting

```text
relevance
price_low
price_high
rating
```

### Pagination

```text
page
size
```

### Facets

```text
categories
brands
price stats
```

### Autocomplete

```text
GET /products/autocomplete?q=...
```

### Typo tolerance

```text
headphons
```

should find:

```text
headphones
```

### Analytics

Dashboard should show:

```text
products by category
products by brand
average price
average rating
price distribution
```

### Advanced

Eventually:

```text
semantic search
+
hybrid search
```

---

# 112. What You Should Be Able to Explain in an Interview

You should be able to answer:

### What is OpenSearch?

A distributed search and analytics engine built on Apache Lucene.

### Why use OpenSearch instead of PostgreSQL search?

For advanced full-text search, relevance ranking, faceting, distributed search, analytics, and vector search use cases.

### What is an index?

A logical collection of documents.

### What is a document?

A JSON record stored in an index.

### What is a mapping?

The schema-like definition describing how fields are indexed and interpreted.

### `text` vs `keyword`?

`text` is primarily for analyzed full-text search. `keyword` is primarily for exact matching, filtering, sorting, and aggregations.

### What is a shard?

A physical partition of an index backed by a Lucene index.

### What is a replica?

A copy of a primary shard used for resilience and additional search capacity.

### Why use filters?

Filters restrict matching documents without being intended to contribute to relevance scoring.

### What is an aggregation?

A way to calculate summaries and statistics over documents.

### Why is relevance important?

Search engines need to rank matching documents rather than merely return an unordered set.

### What is an analyzer?

A pipeline that transforms text into searchable tokens.

### What is vector search?

Search based on vector similarity, generally enabling semantic rather than purely lexical matching.

### What is hybrid search?

Combining lexical and semantic/vector retrieval.

---

# 113. One Mental Model to Remember

If you remember only one diagram, remember this:

```text
                    OPEN SEARCH
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
       Storage         Search        Analytics
          |              |              |
       Documents       Query DSL     Aggregations
       Mappings        Relevance     Dashboards
       Shards          Analyzer      SQL/PPL
       Replicas        BM25
          |              |
          +------+-------+
                 |
                 v
           Application
                 |
                 v
              FastAPI
                 |
                 v
               Users
```

And for AI search:

```text
                  USER QUERY
                      |
             +--------+--------+
             |                 |
             v                 v
       Keyword Search     Vector Search
             |                 |
             v                 v
         BM25-ish          k-NN
         relevance       similarity
             |                 |
             +--------+--------+
                      |
                      v
                 Hybrid Rank
                      |
                      v
                   Results
```

---

# 114. Final Checklist

Mark these off as you learn them.

## Fundamentals

- [ ] I understand cluster
- [ ] I understand node
- [ ] I understand index
- [ ] I understand document
- [ ] I understand mapping
- [ ] I understand shard
- [ ] I understand replica

## Local Setup

- [ ] Docker installed
- [ ] OpenSearch running
- [ ] Dashboards running
- [ ] Can check cluster health
- [ ] Can inspect indexes

## CRUD

- [ ] Create index
- [ ] Create document
- [ ] Read document
- [ ] Update document
- [ ] Delete document
- [ ] Bulk indexing

## Search

- [ ] match
- [ ] term
- [ ] match_phrase
- [ ] bool
- [ ] filter
- [ ] should
- [ ] must_not
- [ ] range
- [ ] exists
- [ ] fuzzy
- [ ] wildcard
- [ ] prefix
- [ ] multi_match

## Relevance

- [ ] Analyzer
- [ ] Tokenizer
- [ ] Token filters
- [ ] BM25 concept
- [ ] Boosting
- [ ] Explain API

## Analytics

- [ ] Terms aggregation
- [ ] Average
- [ ] Min/max
- [ ] Stats
- [ ] Histogram
- [ ] Faceted search

## Operations

- [ ] Shards
- [ ] Replicas
- [ ] Refresh
- [ ] Segments
- [ ] Aliases
- [ ] Templates
- [ ] Snapshots
- [ ] Monitoring

## Application

- [ ] Python client
- [ ] FastAPI
- [ ] Search endpoint
- [ ] Filters
- [ ] Sorting
- [ ] Pagination
- [ ] Facets
- [ ] Autocomplete

## AI Search

- [ ] Embeddings
- [ ] Vector index
- [ ] k-NN
- [ ] Semantic search
- [ ] Hybrid search
- [ ] Reranking

---

# 115. Official Documentation

Use the official OpenSearch documentation as the source of truth for version-specific configuration and APIs:

- OpenSearch Getting Started
- OpenSearch Docker installation
- OpenSearch Dashboards
- Query DSL
- Aggregations
- Index management
- Security
- Vector search

Because OpenSearch evolves quickly, always check the documentation for the exact version used by your Docker image before copying production configuration.

---

# 116. The Best Way to Study This

Don't read this document from top to bottom like a textbook.

Use this loop:

```text
READ
  |
  v
RUN THE API
  |
  v
CHANGE THE QUERY
  |
  v
BREAK SOMETHING
  |
  v
READ THE MAPPING
  |
  v
RUN _ANALYZE
  |
  v
USE DASHBOARDS
  |
  v
BUILD THE FEATURE
```

The moment you find yourself thinking:

> "Why the hell did OpenSearch return THAT document?"

you are learning the good stuff.

Search engineering starts where `match_all` ends.
