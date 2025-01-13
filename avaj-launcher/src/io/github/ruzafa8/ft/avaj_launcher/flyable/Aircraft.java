package io.github.ruzafa8.ft.avaj_launcher.flyable;

import io.github.ruzafa8.ft.avaj_launcher.Coordinates;
import io.github.ruzafa8.ft.avaj_launcher.OutputFileWriter;

public class Aircraft extends Flyable {
    protected long id;
    protected String name;
    protected Coordinates coordinates;

    protected Aircraft(long id, String name, Coordinates coordinates) {
        this.id = id;
        this.name = name;
        this.coordinates = coordinates;
    }

    @Override
    public void updateConditions() {
        if (this.coordinates.getHeight() == 0) {
            OutputFileWriter.write(getCode() + " landing.");
            this.weatherTower.unregister(this);
            this.weatherTower = null;
        }
    }

    @Override
    public String getCode() {
        return this.getClass().getSimpleName() + '#' + name + '(' + id + ")";
    }
}
