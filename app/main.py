from fastapi import FastAPI,HTTPException
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
app = FastAPI()
resource = Resource(attributes={
    SERVICE_NAME: "sec"
})

jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831,
)

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(jaeger_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
FastAPIInstrumentor.instrument_app(app)
#promi
from prometheus_fastapi_instrumentator import Instrumentator
instrumentator = Instrumentator().instrument(app)

@app.on_event("startup")
async def _startup():
    instrumentator.expose(app)
@app.get("/health")
def health():
    return
@app.get("/1_nya")
def read_root():
    return {"result":"NYA KAWAI"}
@app.get("/1_poka")
def read_root():

    return {"result":"USSSR"}