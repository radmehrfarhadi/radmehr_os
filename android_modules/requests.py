import json as _json
import urllib.error
import urllib.request


class RequestException(Exception):
    pass


class HTTPError(RequestException):
    pass


class Response:
    def __init__(self, status_code, body, headers=None):
        self.status_code = status_code
        self._body = body
        self.headers = headers or {}

    @property
    def text(self):
        return self._body.decode("utf-8", errors="replace")

    def json(self):
        return _json.loads(self.text)

    def raise_for_status(self):
        if not 200 <= self.status_code < 400:
            raise HTTPError(f"HTTP {self.status_code}: {self.text[:200]}")


def _request(method, url, headers=None, json=None, timeout=60):
    data = None
    request_headers = dict(headers or {})

    if json is not None:
        data = _json.dumps(json).encode("utf-8")
        request_headers.setdefault("Content-Type", "application/json")

    req = urllib.request.Request(
        url,
        data=data,
        headers=request_headers,
        method=method,
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return Response(
                response.getcode(),
                response.read(),
                dict(response.headers.items()),
            )
    except urllib.error.HTTPError as exc:
        body = exc.read() if hasattr(exc, "read") else b""
        return Response(exc.code, body, dict(exc.headers.items()) if exc.headers else {})
    except (urllib.error.URLError, OSError, TimeoutError) as exc:
        raise RequestException(str(exc)) from exc


def get(url, headers=None, timeout=60, **kwargs):
    return _request("GET", url, headers=headers, timeout=timeout)


def post(url, headers=None, json=None, timeout=60, **kwargs):
    return _request("POST", url, headers=headers, json=json, timeout=timeout)
