library(shiny)
library(flametree)
library(colourpicker)
library(ggplot2)

ui <- fluidPage(
  titlePanel("Interactive Flametree Explorer"),
  sidebarLayout(
    sidebarPanel(
      sliderInput("time", "Growth time:", min = 1, max = 10, value = 5),
      sliderInput("trees", "Number of trees:", min = 1, max = 15, value = 5),
      
      colourInput("colour1", "Colour 1:", "#1E2640"),
      colourInput("colour2", "Colour 2:", "#F3EAC0"),
      colourInput("colour3", "Colour 3:", "#DC9750"),
      colourInput("colour4", "Colour 4:", "#922C40"),
      colourInput("bg", "Background colour:", "antiquewhite"),
      
      selectInput("style", "Style:", choices = c("plain", "nativeflora"), selected = "plain"),
      
      actionButton("generate", "Generate"),
      downloadButton("downloadPlot", "Save Image")
    ),
    
    mainPanel(
      plotOutput("flamePlot", height = "600px", width = "100%")
    )
  )
)

server <- function(input, output, session) {
  
  flame_data <- eventReactive(input$generate, {
    dat <- flametree_grow(time = input$time, trees = input$trees)
    palette <- c(input$colour1, input$colour2, input$colour3, input$colour4)
    list(dat = dat, palette = palette, bg = input$bg, style = input$style)
  })
  
  # Render interactive plot
  output$flamePlot <- renderPlot({
    req(flame_data())
    flame <- flame_data()
    
    ggplot_obj <- flametree_plot(
      data       = flame$dat,
      palette    = flame$palette,
      background = flame$bg,
      style      = flame$style
    )
    
    print(ggplot_obj)
  })
  
  # Download handler
  output$downloadPlot <- downloadHandler(
    filename = function() {
      paste0("flametree_", Sys.Date(), ".png")
    },
    content = function(file) {
      flame <- flame_data()
      ggplot_obj <- flametree_plot(
        data       = flame$dat,
        palette    = flame$palette,
        background = flame$bg,
        style      = flame$style
      )
      
      # Save using ggsave
      ggsave(
        filename = file,
        plot     = ggplot_obj,
        width    = 10,
        height   = 10,
        units    = "in",
        dpi      = 300
      )
    }
  )
}

shinyApp(ui, server)
