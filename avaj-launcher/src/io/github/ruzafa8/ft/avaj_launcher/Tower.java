package io.github.ruzafa8.ft.avaj_launcher;

import io.github.ruzafa8.ft.avaj_launcher.flyable.Flyable;

import java.util.ArrayList;
import java.util.List;

public class Tower {
    protected final List<Flyable> observers = new ArrayList<>();

    public void register(Flyable observer) {
        this.observers.add(observer);
        OutputFileWriter.write("Tower says: " + observer.getCode() + " registered to weather tower.");
    }

    public void unregister(Flyable observer) {
        this.observers.remove(observer);
        OutputFileWriter.write("Tower says: " + observer.getCode() + " unregistered from weather tower.");
    }

    protected void conditionChanged() {
        int i = 0;
        while (i < this.observers.size()) {
            Flyable observer = this.observers.get(i);
            observer.updateConditions();
            if (observer.getWeatherTower() != null)
                i++;
        }
    }
}
