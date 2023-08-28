api_gateway/
│
├── api/
│   ├── v1/
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── products.py
│   │   │   └── ... (otros módulos para diferentes recursos si los agregas)
│   │   │
│   │   ├── dependencies/
│   │   │   ├── authentication.py
│   │   │   └── ... (otros módulos para diferentes dependencias)
│   │   │
│   │   ├── __init__.py
│   │   └── routers.py
│   │
│   └── __init__.py
│
├── core/
│   ├── config.py
│   └── utils.py
│
├── tests/
│   └── ...
│
└── main.py