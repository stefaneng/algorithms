class Activity {
    private int start;
    private int finish;

    public Activity(int start, int finish) {
        this.start = start;
        this.finish = finish;
    }

    public getStart() {
        return start;
    }

    public getFinish() {
        return finish;
    }

    @Override
    public String toString() {
        return "Start time: " + start + " Finish time: " + finish;
    }
}
