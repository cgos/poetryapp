package poetrywebapp;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import poetrywebapp.dto.PoetBioDTO;
import poetrywebapp.dto.PoetryDTO;

@CrossOrigin(origins = "*")
@RestController
public class PoetryController {
	private org.slf4j.Logger logger = org.slf4j.LoggerFactory.getLogger(PoetryController.class);
	
	@Value("${poemprovider.api.url}")
	private String poemProviderApiUrl;
	
	@Value("${poetbio.api.url}")
	private String poetBioApiUrl;
	
	@GetMapping("/poetry")
	@ResponseBody
	public PoetryDTO poetry() {
		logger.info("/poetry");
		RestTemplate restTemplate = new RestTemplate();
		PoetryDTO dto = restTemplate.getForObject(poemProviderApiUrl, PoetryDTO.class);
		PoetBioDTO bio = restTemplate.getForObject(poetBioApiUrl, PoetBioDTO.class);
		dto.setBio(bio.getBio());
		logger.info(dto.toString());
		return dto;
	}
	
}
