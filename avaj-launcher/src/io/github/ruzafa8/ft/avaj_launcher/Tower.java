package io.github.ruzafa8.ft.avaj_launcher;

import java.util.LinkedList;
import java.util.List;

public class Tower {
    private final List<Flyable> observers = new LinkedList<>();

    public void register(Flyable observer) {
        this.observers.add(observer);
    }

    public void unregister(Flyable observer) {
        this.observers.remove(observer);
    }

    protected void conditionChanged() {

    }
}
