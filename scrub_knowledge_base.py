from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue

# 1. Connect to your local Qdrant container
qdrant_client = QdrantClient(url="http://localhost:6333")
collection_name = "alphalearn_curriculum"

print(f"🧹 Commencing data purge on collection: '{collection_name}'...")

# 2. Define a metadata filter to isolate the target data
# We are targeting the 'Safety Guardrails' topic to simulate purging leaked files
purge_filter = Filter(
    must=[
        FieldCondition(
            key="topic", 
            match=MatchValue(value="Safety Guardrails")
        )
    ]
)

# 3. Execute the delete operation across the cluster
delete_result = qdrant_client.delete(
    collection_name=collection_name,
    points_selector=purge_filter
)

print("✅ Data successfully scrubbed from vector memory stores!")
print(delete_result)

