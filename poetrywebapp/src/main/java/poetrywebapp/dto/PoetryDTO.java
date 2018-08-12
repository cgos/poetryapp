package poetrywebapp.dto;

public class PoetryDTO {

	private int id = 0;
	private String poem;
	private String title;
	private String author;
	private String bio;
	
	public String getBio() {
		return bio;
	}

	public void setBio(String bio) {
		this.bio = bio;
	}

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
		return "PoetryDTO [id=" + id + ", poem=" + poem + ", title=" + title
				+ ", author=" + author + "bio= " + bio + "]";
	}
}
