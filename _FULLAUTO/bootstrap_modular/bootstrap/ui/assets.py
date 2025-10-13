
OPTIONS_JS = """// Shared options for DBs and AI models
window.APP_OPTIONS = {
  dbs: [
    { key: "sqlite", label: "SQLite", devDefault: true },
    { key: "mongodb", label: "MongoDB" },
    { key: "postgres", label: "PostgreSQL" },
    { key: "mysql", label: "MySQL" },
    { key: "mariadb", label: "MariaDB" },
    { key: "redis", label: "Redis" },
    { key: "elasticsearch", label: "Elasticsearch" },
    { key: "neo4j", label: "Neo4j" }
  ],
  aiModels: {
    openai: ["gpt-4o","gpt-4o-mini","o4-mini","gpt-4-turbo","gpt-3.5-turbo"],
    anthropic: ["claude-3-opus","claude-3-sonnet","claude-3-haiku"],
    google: ["gemini-1.5-pro","gemini-1.5-flash","palm-2"],
    mistral: ["mistral-large","mistral-medium","mistral-small","mixtral-8x7b"]
  },
  clients: ["Agence","Client Alpha","Client Beta","Client Gamma"]
};
"""
