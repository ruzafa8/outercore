class Tower {
    private List<Flyable> observers = new LinkedList<>();

    public void register(Flyable pFlyable) {
        this.observers.add(pFlyable);
    }

    public void unregister(Flyable pFlyable) {
        this.observers.remove(pFlyable);
    }

    protected void conditionChanged();
}
