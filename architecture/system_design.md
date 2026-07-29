# 🏛️ Climate Guardian AI System Architecture

## Component Overview

1. **Ingestion API**: Built with FastAPI to handle streaming SSE connections from satellite feeds and IoT sensor streams.
2. **LangGraph State Machine**: Controls the multi-agent graph state transition:
   - `IngestionNode` -> `VisionAgent` -> `RiskAssessmentAgent` -> `ActionPlanner`.
3. **Qdrant Vector Storage**: Stores IPCC report embeddings (1536-dim vectors) using cosine similarity metric.
4. **Safety Filter**: Pydantic input-sanitizer for prompt injection detection.
