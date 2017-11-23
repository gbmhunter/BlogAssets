class ICallback {
public:
    virtual void Call() = 0;
    virtual ~ICallback() {};
};

class Example {
public:
    void GiveCallback(ICallback* callback) {
        callback_ = callback;
    }

    void CallCallback() {
        callback_->Call();
    }

    ICallback * callback_;
};
