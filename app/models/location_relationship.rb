class LocationRelationship < ActiveRecord::Base
  attr_accessible :child_location_id, :parent_location_id
end
