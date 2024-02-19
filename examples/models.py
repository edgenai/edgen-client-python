#!/usr/bin/env python

from edgen import Edgen

client = Edgen()

def main() -> None:

    models = client.models.list()

    print(f"Models listing")
    print(f"==============")
    for m in models:
        print(f"id     : {m.id}")
        print(f"created: {m.created}")
        print(f"object : {m.object}")
        print(f"owner  : {m.owned_by}")

    print("")

    try:
        model = client.models.retrieve("TheFake%2fMy-fake-model-GGUF")
        print(f"One model")
        print(f"=========")
        print(f"id     : {model.id}")
        print(f"created: {model.created}")
        print(f"object : {model.object}")
        print(f"owner  : {model.owned_by}")
    except Exception as e:
        print(f"cannot retriev model: {e}")

    print("")

    try:
        model = client.models.delete("TheFake%2fMy-fake-model-GGUF")
        print(f"Deleted model")
        print(f"=============")
        print(f"id     : {model.id}")
        print(f"object : {model.object}")
        print(f"deleted: {model.deleted}")
    except Exception as e:
        print(f"cannot delete model: {e}")

if __name__ == "__main__":
    main()
