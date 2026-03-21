#!/usr/bin/env python3
"""
Скрипт для загрузки базы знаний из папки knowledge_base
"""

import os
from dotenv import load_dotenv
from embeddings import EmbeddingStore, load_documents_from_folder

load_dotenv()

print("=" * 70)
print("📚 ЗАГРУЗКА БАЗЫ ЗНАНИЙ")
print("=" * 70)

# Инициализируем хранилище
embedding_store = EmbeddingStore(collection_name="rag_documents")

# Проверяем, есть ли уже документы
current_count = embedding_store.collection.count()
if current_count > 0:
    print(f"\n⚠️  В базе уже есть {current_count} документов")
    response = input("Очистить базу и загрузить новые документы? (y/n): ")
    if response.lower() == 'y':
        print("Очистка базы...")
        embedding_store.clear_collection()
    else:
        print("Отмена загрузки")
        exit(0)

# Загружаем документы из папки
kb_path = "./knowledge_base"
print(f"\n📂 Загрузка документов из {kb_path}...")

docs = load_documents_from_folder(kb_path)

if docs:
    print(f"\n✓ Найдено {len(docs)} документов")
    print("\nДобавление в базу знаний...")
    embedding_store.add_documents(docs)
    print(f"\n✅ Готово! В базе теперь {embedding_store.collection.count()} документов")
else:
    print("❌ Документы не найдены")

print("=" * 70)
