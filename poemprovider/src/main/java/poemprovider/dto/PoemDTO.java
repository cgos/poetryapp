package poemprovider.dto;

public class PoemDTO {
	private int id = 0;
	private String poem = "While you are preparing for sleep, brushing your teeth,<br /> or riffling through a magazine in bed,<br /> the dead of the day are setting out on their journey.<br /> <br /> They're moving off in all imaginable directions,<br /> each according to his own private belief,<br /> and this is the secret that silent Lazarus would not reveal:<br /> that everyone is right, as it turns out.<br /> you go to the place you always thought you would go,<br /> The place you kept lit in an alcove in your head.<br /> <br /> Some are being shot into a funnel of flashing colors<br /> into a zone of light, white as a January sun.<br /> Others are standing naked before a forbidding judge who sits<br /> with a golden ladder on one side, a coal chute on the other.<br /> <br /> Some have already joined the celestial choir<br /> and are singing as if they have been doing this forever,<br /> while the less inventive find themselves stuck<br /> in a big air conditioned room full of food and chorus girls.<br /> <br /> Some are approaching the apartment of the female God,<br /> a woman in her forties with short wiry hair<br /> and glasses hanging from her neck by a string.<br /> With one eye she regards the dead through a hole in her door.<br /> <br /> There are those who are squeezing into the bodies<br /> of animals--eagles and leopards--and one trying on<br /> the skin of a monkey like a tight suit,<br /> ready to begin another life in a more simple key,<br /> <br /> while others float off into some benign vagueness,<br /> little units of energy heading for the ultimate elsewhere.<br /> <br /> There are even a few classicists being led to an underworld<br /> by a mythological creature with a beard and hooves.<br /> He will bring them to the mouth of the furious cave<br /> guarded over by Edith Hamilton and her three-headed dog.<br /> <br /> The rest just lie on their backs in their coffins<br /> wishing they could return so they could learn Italian<br /> or see the pyramids, or play some golf in a light rain.<br /> They wish they could wake in the morning like you<br /> and stand at a window examining the winter trees,<br /> every branch traced with the ghost writing of snow.<br /> <br /> (And some just smile, forever on)";;
	private String title = "The Afterlife";
	private String author = "Billy Collins";
	
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}
	
	public String getPoem() {
		return poem;
	}
	
	public void setPoem(String poem) {
		this.poem = poem;
	}
	
	public String getTitle() {
		return title;
	}
	
	public void setTitle(String title) {
		this.title = title;
	}
	
	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}
	
	@Override
	public String toString() {
		return "PoemDTO [id=" + id + ", poem=" + poem + ", title=" + title
				+ ", author=" + author + "]";
	}

}
