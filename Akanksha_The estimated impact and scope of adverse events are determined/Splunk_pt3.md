<h1>Monitor and investigate alerts from the Alerts tab🔔</h1>

Investigate triggered alerts from the Alerts tab. When you view alerts from here, you can filter the list by dimensions of entities or groups to search for triggered alerts that 
are affecting entities or groups of similar dimensions.

A color-coded severity status displays the state of the alert. This allows you to easily view the state of the alert by color. Severity colors include: Green for Information,
Yellow for Medium, and Red for Critical. A severity status arrow displays alongside the severity status color in the Current Severity column, indicating whether the alert has 
improved or degraded recently.The row size in the Alerts tab is limited to two rows per entity. If resizing the window, or if the slide-out panel is activated, the dimensions 
column truncates and only displays dimensions that fit into the available two-row column size. 

The row does not expand or wrap to more than two rows, so all dimensions might not 
display. To view all of the dimensions for each entity or group, close the slide-out panel or resize your window to a larger view.

**To start investigating an alert, follow these steps:**

**1)** Go to the Alerts tab.<br>

**2**)Select the Entities or Groups view to investigate entities or groups, respectively.<br>

**3)**(Optional) Filter for triggered alerts according by entity dimensions or group names to find triggered alerts for specific types of entities or groups. This enables you to 
monitor triggered alerts for specific dimensions across entities and groups.<br>

**4)** Select an entity or group, depending on the view you selected. From the list of triggered alerts in the slide-out panel on the right side of the page, view the triggered alerts
for the selected entity or group. The slide-out panel displays every triggered alert for the entity or group you selected.<br>

**5)** For the alert that you want to investigate, click the This screen image shows the More icon. icon and select Investigate. This takes you to the Analysis Workspace for the alert.<br>

**6)**(For admins and power users) To view the alert configuration and learn more about what the alert is tracking, click the This screen image shows the More icon. icon and select
Clone this Panel. From the cloned alert panel, you can modify Aggregations for the alert's metric, modify the Split by dimension for the alert's metric, display a Time comparison
for the alert's metric, and Filter the alert's metric by dimension.<br>
<hr>
<h2>Alert notifications</h2>
  
When an alert is created by an administrator, there is an option to include an alert notification. This can be an alert notification sent by email or using VictorOps for Splunk. 
When the alert triggers, one or more notifications are sent depending on the type of alert notification and recipients selected during the alert creation, including:
<br>

-An email notification with details of the alert.<br>
-A VictorOps notification, with the details displaying in your VictorOps account timeline. In your VictorOps account, **click Alert Payload** link to view details of the alert.<br>

<h2>Alert details</h2>

Select an alert from the Alerts tab or the Analysis Workspace to view its details. These details include the threshold conditions and severity levels configured for the alert,
settings, and triggered instances. Triggered instances appear as This screen image shows the triggered instance chart annotation. annotations on the chart, and up to 100 
annotations can display on the chart. Triggered instance annotations appear at the time the alert triggers, not the precise time the alert threshold is crossed.<br>

Alert badges🔔 This screen image shows the gray alert badge. gauge the alert severity level. To help you monitor alert activity, badge colors are based on the most recent severity
level of a triggered alert.

![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/100219040/9fa1e037-dc46-4f67-b5bf-5f3afeed3d90)

<h2>Example</h2>
The following alert shows CPU user average for the cpu.user metric.

![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/100219040/e76b9410-20c2-4342-906e-f2814ba0861f)

This screen image shows a chart of an alert for CPU Overutilization for the cpu.system metric.
This alert is based on the aggregate average of cpu.user metric values. The green alert badge indicates a severity level of Info, yellow for medium, and red for critical. 
The horizontal lines show the alert threshold values. The This screen image shows the triggered instance chart annotation. annotations show triggered instances for the alert.
