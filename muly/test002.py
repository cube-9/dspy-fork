import dspy
from dspy.datasets.gsm8k import GSM8K, gsm8k_metric
import phoenix as px
from pydantic import BaseModel, Field

# Set up the LM
turbo = dspy.OpenAI(model='gpt-3.5-turbo-instruct', max_tokens=250)
dspy.settings.configure(lm=turbo)


px.launch_app()

from openinference.instrumentation.dspy import DSPyInstrumentor
from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

endpoint = "http://127.0.0.1:6006/v1/traces"
resource = Resource(attributes={})
tracer_provider = trace_sdk.TracerProvider(resource=resource)
span_otlp_exporter = OTLPSpanExporter(endpoint=endpoint)
tracer_provider.add_span_processor(SimpleSpanProcessor(span_exporter=span_otlp_exporter))
trace_api.set_tracer_provider(tracer_provider=tracer_provider)
DSPyInstrumentor().instrument()

deal_terms = "2 free month, 50% discount next 3 month."

class DealTerms(dspy.Signature):
    """Analyze deal terms and describe the discount for each month."""

    deal_terms = dspy.InputField(desc="Deal terms as free text may include free months, discounts, etc. may include spelling errors.")
    description_invoice_month_1 = dspy.OutputField(desc="Description of the invoice for month 1")
    description_invoice_month_2 = dspy.OutputField(desc="for month 2")
    description_invoice_month_3 = dspy.OutputField(desc="3")
    description_invoice_month_4 = dspy.OutputField(desc="4")
    description_invoice_month_5 = dspy.OutputField(desc="5")
    description_invoice_month_6 = dspy.OutputField(desc="6")
    description_invoice_month_7 = dspy.OutputField(desc="7")
    description_invoice_month_8 = dspy.OutputField(desc="8")
    description_invoice_month_9 = dspy.OutputField(desc="9")
    description_invoice_month_10 = dspy.OutputField(desc="10")
    description_invoice_month_11 = dspy.OutputField(desc="11")
    description_invoice_month_12 = dspy.OutputField(desc="12")
        
terms = dspy.ChainOfThought(DealTerms)
res = terms(deal_terms=deal_terms)

print(res)

