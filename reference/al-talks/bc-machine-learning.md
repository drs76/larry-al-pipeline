# bc-machine-learning

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: NAV TechDays 2019 - How to make AI work for your Business... | 2026-07-27 -->
### BC built-in ML/AI frameworks (NAV TechDays 2019, Dmitry — searchable, unverified)

Four prebuilt frameworks in BC for consuming Azure ML models. Each wraps auth + schema marshalling to an Azure ML web service; underneath it's just HTTP request/response, so a non-Azure prediction service can be called with plain HTTP instead.

**Core ML terms**
- *Features* = input columns that influence the prediction. *Label* = the single column you predict.
- *Regression* algorithms → predict a numeric (decimal/integer) value. *Classification* algorithms → predict a value from a fixed list (two-class for boolean yes/no, multi-class for larger list). Pick algorithm type by output shape.
- Empty/blank cells break training — rows with any blank feature get skipped. Fix: replace blanks with a placeholder (e.g. `NA`) before training. In Azure ML Studio use the *Clean Missing Data* module; also *Remove Duplicate Rows* for conflicting rows (same key, different label).
- Model quality = accuracy measured by splitting data (e.g. 80% train / 20% test), predicting the held-out past, comparing to actuals (coefficient of determination). Quality depends on the test split, not just the model.

**1. Time Series API**
- Codeunit `Time Series Management` [sic? — verify name/ID on Learn]. Used by Inventory/Sales Forecast and Cash Flow Forecast extensions (since ~NAV 2017).
- Only two features: a date field + one master key (e.g. item no.); label = quantity/amount. Because only date+key are used, forecasts often come out flat across the horizon — no other signals considered.
- Uses statistical extrapolation algorithms ARIMA, ETS, STL [sic? captions — verify], plus combination modes that average them.
- Flow: `Initialize`(uri,key) → `PrepareData` (fills a predefined buffer table; specify which field is the group/period key and which is the date, plus period type + count of history) → `Forecast`(numberOfPeriods) → read result buffer. Sends full history on every call.
- Model source: an Azure AI Gallery experiment; open in ML Studio (classic) after creating a *Machine Learning Studio (classic) workspace*, then *Deploy Web Service* to get uri+key.

**2. ML Prediction API**
- Codeunit `ML Prediction Management`, called via codeunit ~2003 [sic? — verify ID/name]. Powers the Late Payment Prediction extension.
- Supports up to ~20 additional features (limit). Uses tree/regression algorithms (ANOVA-family) [sic? — verify].
- Two-phase: **train once** → model returned as a base64 text blob (kilobytes) + a quality score; store the blob in BC (any blob/text field). **Predict** by sending the stored model + future feature values — no need to resend history each time.
- Can return an explanation PDF from Azure ML showing the decision tree (the learned if/else splits).
- Train: set source record/table, specify feature columns + label, call train. Predict: set same features + same label as training, call predict, read forecast buffer.

**3. Custom Azure ML API**
- Codeunit `Azure ML Connector` / codeunit 201 [sic? — verify]. For fully custom models built from scratch in Azure ML Studio.
- BC holds no model and sends no history — the trained prediction web service lives entirely in Azure; BC just posts feature values per request.
- Specify uri, key, input schema name + output name (default `input1`/`output1`), and input column names matching the web service input schema. Response is JSON; extract prediction as text and convert.
- Studio build flow: import data → (optional) feature engineering/clean → split train/test → Train Model (one param: the label column) → Score Model (predict on test set) → Evaluate Model (quality) → deploy predictive web service (define web service input/output schema, no code). Presenter got better results with Boosted Decision Tree Regression + more features.
- Algorithm selection reference: search "Azure ML algorithm cheat sheet".

**4. Custom Vision API**
- Codeunit exposing `Image Analysis Management` + `Image Analysis Result` [sic? — verify], plus a BC camera/take-picture capability to capture and post an image to a trained Custom Vision model at customvision.ai (uri + prediction key). Returns tags/classification.
- Retrain by tagging images and re-publishing; there is a Custom Vision API to automate retraining.
- Gotcha ("tank/sky" cautionary tale): image classifiers can latch onto background/lighting instead of the subject — validate on realistic varied backgrounds. Demo misclassified fresh vs. spoiled apple due to lighting/background.

**Ops notes**
- All frameworks except cloud image capture ran against a local Docker BC in the demo (on-prem capable).
- Automate periodic retraining via Job Queue.
- For recommendations/decision/path-finding beyond prediction, look at Azure Cognitive Services.
- Hybrid approach: split a hard task into ML-solved and classically-coded sub-tasks, then combine.
