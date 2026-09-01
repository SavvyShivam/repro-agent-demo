from flask import Flask, jsonify, request

app = Flask(__name__)

WIDGETS = [{"id": i, "name": f"widget-{i}"} for i in range(1, 6)]


@app.get("/widgets")
def list_widgets():
    limit = request.args.get("limit", type=int)
    items = WIDGETS
    if limit:  # BUG: limit=0 is falsy, so the cap is ignored and all rows return
        items = WIDGETS[:limit]
    return jsonify(items)


if __name__ == "__main__":
    app.run(port=5000)
