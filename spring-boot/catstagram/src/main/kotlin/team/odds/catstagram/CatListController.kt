package team.odds.catstagram

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController

@RestController
class CatListController {

    @GetMapping("/cats")
    fun getCat(): Array<String> {
        val cats: Array<String> = arrayOf<String>("Salee", "Marble")
        return cats
    }

}